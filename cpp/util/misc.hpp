#ifndef UTIL_MISC_HPP
#define UTIL_MISC_HPP
#include <functional>
#include <sstream>
#include <string>
#include <vector>
#include <set>

#include <kj/async.h>
#include <kj/debug.h>
#include <kj/string.h>

namespace util {
template <typename Out>
void split(const std::string& s, char delim, Out result) {
  std::stringstream ss(s);
  std::string item;
  while (std::getline(ss, item, delim)) {
    if (!item.empty()) *(result++) = item;
  }
}

inline std::vector<std::string> split(const std::string& s, char delim) {
  std::vector<std::string> elems;
  split(s, delim, std::back_inserter(elems));
  return elems;
}

inline std::function<bool()> setBool(bool& var) {
  return [&var]() {
    var = true;
    return true;
  };
};

inline std::function<bool(kj::StringPtr)> setString(std::string& var) {
  return [&var](kj::StringPtr p) {
    var = p;
    return true;
  };
};

inline std::function<bool(kj::StringPtr)> setInt(int& var) {
  return [&var](kj::StringPtr p) {
    var = std::stoi(std::string(p));
    return true;
  };
};

class UnionPromiseBuilder {
  struct Info {
    bool fatalFailure;
    size_t resolved = 0;
    std::vector<kj::Promise<void>> promises;
    bool finalized = false;
    std::multiset<std::string> pending;
  };

 public:
  UnionPromiseBuilder(bool fatalFailure = true)
      : p_(kj::newPromiseAndFulfiller<void>()) {
    auto info = kj::heap<Info>();
    info_ = info.get();
    info_->fatalFailure = fatalFailure;
    fulfiller_ = p_.fulfiller.get();
    p_.promise = p_.promise.attach(std::move(info), std::move(p_.fulfiller));
  }

  void AddPromise(kj::Promise<void> p, std::string what = "unanamed") {
    info_->pending.insert(what);
    info_->promises.push_back(
        std::move(p)
            .then(
                [this, info = info_, fulfiller = fulfiller_, what]() {
                  info->resolved++;
                  info->pending.erase(info->pending.find(what));
//                  if (!info->fatalFailure) {
//                    KJ_DBG("XXX Promise success", info->resolved,
//                           info->promises.size(), what);
//                    PrintRemainig();
//                  }
                  if (info->finalized &&
                      info->resolved == info->promises.size()) {
                    fulfiller->fulfill();
                  }
                },
                [this, fulfiller = fulfiller_, info = info_,
                 idx = info_->promises.size(), what](kj::Exception exc) {
                  info->pending.erase(info->pending.find(what));
                  // Cancel all other promises
                  if (info->fatalFailure) {
                    fulfiller->reject(kj::cp(exc));
                  } else {
                    info->resolved++;
//                    KJ_DBG("XXX Promise failed", info->resolved,
//                           info->promises.size(), what);
//                    PrintRemainig();
                    if (info->finalized &&
                        info->resolved == info->promises.size()) {
                      fulfiller->fulfill();
                    }
                  }
                  return exc;
                })
            .eagerlyEvaluate(nullptr));
  }

  kj::Promise<void> Finalize() && KJ_WARN_UNUSED_RESULT {
    info_->finalized = true;
    if (!info_->fatalFailure) {
      KJ_DBG("XXX Finalizing builder", info_->resolved, info_->promises.size());
    }
    if (info_->resolved == info_->promises.size()) {
      fulfiller_->fulfill();
    }
    return std::move(p_.promise);
  }

  int GetMissing() { return info_->promises.size() - info_->resolved; }

  void PrintRemainig() {
    KJ_DBG("YYY Pending promises:");
    for (std::string w : info_->pending)
      KJ_DBG("YYY    ", w);
  }

 private:
  kj::PromiseFulfillerPair<void> p_;
  // TODO use std::move(this) rather that kj::heap
  Info* info_ = nullptr;
  kj::PromiseFulfiller<void>* fulfiller_ = nullptr;
};

}  // namespace util
#endif
