#ifndef UTIL_SHA256_H
#define UTIL_SHA256_H

#include <array>
#include <string>

#include "capnp/sha256.capnp.h"

namespace util {
namespace {
static const constexpr uint32_t DIGEST_SIZE = (256 / 8);
}

class SHA256_t {
  std::array<uint8_t, DIGEST_SIZE> hash_;

 public:
  SHA256_t(const std::array<uint8_t, DIGEST_SIZE>& hash) : hash_(hash) {}
  SHA256_t(capnproto::SHA256::Reader in);
  void ToCapnp(capnproto::SHA256::Builder out);

  std::string Hex() const;

  bool isZero() const {
    for (uint32_t i = 0; i < DIGEST_SIZE; i++)
      if (hash_[i]) return false;
    return true;
  }
};

class SHA256 {
 public:
  SHA256() : m_block{}, m_h{} { init(); }
  void init();
  void update(const unsigned char* message, unsigned int len);
  void finalize(unsigned char* digest);
  SHA256_t finalize();

 private:
  static const constexpr uint32_t SHA224_256_BLOCK_SIZE = (512 / 8);
  void transform(const unsigned char* message, unsigned int block_nb);
  unsigned int m_tot_len{0};
  unsigned int m_len{0};
  unsigned char m_block[2 * SHA224_256_BLOCK_SIZE];
  uint32_t m_h[8];
};

}  // namespace util
#endif
