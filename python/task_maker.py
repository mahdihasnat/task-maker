#!/usr/bin/env python3

import sys
from collections import namedtuple

import os.path
import signal
from task_maker.args import get_parser, TaskFormat
from task_maker.config import Config
from task_maker.detect_format import find_task_dir
from task_maker.formats import ioi_format, tm_format, terry_format
from task_maker.help import check_help
from task_maker.languages import LanguageManager
from task_maker.manager import get_frontend, spawn_server, spawn_worker
from typing import Any

MainRet = namedtuple("MainRet", ["exitcode", "interface", "stopped"])


def get_task_format(fmt: TaskFormat):
    """
    Get the format class based on the format of the task.
    """
    if fmt == TaskFormat.IOI:
        return ioi_format.IOIFormat
    elif fmt == TaskFormat.TM:
        return tm_format.TMFormat
    elif fmt == TaskFormat.TERRY:
        return terry_format.TerryFormat
    raise ValueError("Format %s not supported" % fmt)


def setup(config: Config):
    """
    This function has to be called as soon as possible and exactly once to setup
    the system.
    """
    check_help(config)
    if config.run_server:
        return spawn_server(config)
    if config.run_worker:
        return spawn_worker(config)

    LanguageManager.load_languages()


def run(config: Config) -> MainRet:
    """
    Execute task-maker on the given configuration.
    """
    task_dir, fmt = find_task_dir(config.task_dir, config.max_depth,
                                  config.format)
    if not fmt:
        raise ValueError(
            "Cannot detect format! It's probable that the task is ill-formed")
    task_format = get_task_format(fmt)

    os.chdir(task_dir)

    if config.clean:
        task_format.clean()
        return MainRet(exitcode=0, interface=None, stopped=False)

    frontend = get_frontend(config)

    stopped = False

    def stop_server(_1: int, _2: Any) -> None:
        nonlocal stopped
        frontend.stopEvaluation()
        stopped = True

    signal.signal(signal.SIGINT, stop_server)
    signal.signal(signal.SIGTERM, stop_server)

    interface = task_format.evaluate_task(frontend, config)
    return MainRet(
        exitcode=len(interface.errors), interface=interface, stopped=stopped)


def main():
    config = Config()
    args = get_parser(False).parse_args()
    config.apply_file()
    config.apply_args(args)
    setup(config)
    sys.exit(run(config).exitcode)


if __name__ == '__main__':
    main()
