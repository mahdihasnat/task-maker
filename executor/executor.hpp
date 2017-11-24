#ifndef EXECUTOR_EXECUTOR_HPP
#define EXECUTOR_EXECUTOR_HPP
#include <functional>
#include <vector>

#include "proto/request.pb.h"
#include "proto/response.pb.h"
#include "proto/sha256.pb.h"
#include "util/file.hpp"

namespace executor {

struct ExecutorOptions {
  enum Kind { LOCAL };
  Kind kind = LOCAL;

  // Options for the local executor.
  // Number of cores to use. If <=0, autodetect.
  int cores = 0;

  // Directory where intermediate files should be stored.
  std::string store_directory = "./files/";
  // Directory where the sandboxes should be created.
  std::string temp_directory = "./temp/";
};

class Executor {
 public:
  using RequestFileCallback =
      std::function<void(const proto::SHA256& hash,
                         const util::File::ChunkReceiver& chunk_receiver)>;

  // Executes a request and returns the response, after possibly using the
  // provided file_callback to load missing files. This method is thread-safe.
  virtual proto::Response Execute(const proto::Request& request,
                                  const RequestFileCallback& file_callback) = 0;
  virtual void GetFile(const proto::SHA256& hash,
                       const util::File::ChunkReceiver& chunk_receiver) = 0;
};

}  // namespace executor

#endif