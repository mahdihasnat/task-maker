#!/usr/bin/env python3

import multiprocessing
import os
import signal
import subprocess
import time
from typing import Any

import daemon
import grpc
from proto.manager_pb2 import StopRequest, CleanTaskRequest

from proto import manager_pb2_grpc
from python import ioi_format, terry_format
from python.args import get_parser, UIS


def manager_process(pipe: Any, manager: str, port: int) -> None:
    try:
        manager_proc = subprocess.Popen(
            [manager, "--port", str(port)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
        pipe.send(None)
    except Exception as exc:  # pylint: disable=broad-except
        pipe.send(exc)
    with daemon.DaemonContext(detach_process=True, working_directory="/tmp"):
        manager_proc.wait()


def spawn_manager(port: int) -> None:
    manager = os.path.dirname(__file__)
    manager = os.path.join(manager, "..", "manager", "manager")
    manager = os.path.abspath(manager)
    parent_conn, child_conn = multiprocessing.Pipe()
    proc = multiprocessing.Process(
        target=manager_process, args=(child_conn, manager, port))
    proc.start()
    exc = parent_conn.recv()
    if exc:
        raise exc
    proc.join()


def get_manager(args):
    manager_spawned = False
    max_attempts = 10
    connect_timeout = 1
    for attempt in range(max_attempts):
        channel = grpc.insecure_channel(
            "localhost:" + str(args.manager_port))
        ready_future = grpc.channel_ready_future(channel)
        try:
            ready_future.result(timeout=connect_timeout)
        except grpc.FutureTimeoutError:
            print("Spawning manager...")
            if not manager_spawned:
                spawn_manager(args.manager_port)
                manager_spawned = True
            time.sleep(0.5)
        else:
            return manager_pb2_grpc.TaskMakerManagerStub(channel)
    raise RuntimeError("Failed to spawn the manager")


def ioi_format_clean(args):
    ioi_format.clean()
    request = CleanTaskRequest()
    request.store_dir = os.path.abspath(args.store_dir)
    request.temp_dir = os.path.abspath(args.temp_dir)
    manager = get_manager(args)
    manager.CleanTask(request)


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()

    os.chdir(args.task_dir)

    if args.clean:
        if args.format == "ioi":
            ioi_format_clean(args)
        elif args.format == "terry":
            raise NotImplementedError("Clean not implemented yet for terry")
        else:
            raise ValueError("Format %s not supported" % args.format)
        return

    if args.format == "ioi":
        request = ioi_format.get_request(args)
    elif args.format == "terry":
        request = terry_format.get_request(args)
    else:
        raise ValueError("Format %s not supported" % args.format)

    manager = get_manager(args)

    # TODO pass to the constructor if the task is terry like
    ui = UIS[args.ui](
        [os.path.basename(sol.path) for sol in request.solutions], args.format)

    if args.format == "ioi":
        ui.set_task_name("%s (%s)" % (request.task.title, request.task.name))
        ui.set_time_limit(request.task.time_limit)
        ui.set_memory_limit(request.task.memory_limit_kb)

        last_testcase = 0
        for subtask_num, subtask in request.task.subtasks.items():
            last_testcase += len(subtask.testcases)
            ui.set_subtask_info(subtask_num, subtask.max_score,
                                sorted(subtask.testcases.keys()))
        ui.set_max_score(sum(subtask.max_score for subtask in
                             request.task.subtasks.values()))
    elif args.format == "terry":
        ui.set_task_name("%s (%s)" % (request.task.title, request.task.name))
        ui.set_max_score(request.task.max_score)
    else:
        raise ValueError("Format %s not supported" % args.format)

    eval_id = None

    def stop_server(signum: int, _: Any) -> None:
        if eval_id:
            ui.stop("Waiting the manager to complete the last job")
            manager.Stop(StopRequest(evaluation_id=eval_id))
        ui.fatal_error("Aborted with sig%d" % signum)

    signal.signal(signal.SIGINT, stop_server)
    signal.signal(signal.SIGTERM, stop_server)

    if args.format == "ioi":
        events = manager.EvaluateTask(request)
    elif args.format == "terry":
        events = manager.EvaluateTerryTask(request)
    else:
        raise NotImplementedError("Format %s not supported" % args.format)

    for event in events:
        event_type = event.WhichOneof("event_oneof")
        if event_type == "evaluation_started":
            eval_id = event.evaluation_started.id
        elif event_type == "evaluation_ended":
            eval_id = None
        ui.from_event(event)
    ui.print_final_status()


if __name__ == '__main__':
    main()
