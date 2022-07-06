class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

s = Solution()
n = 0b11111111111111111111111111111101
r = s.reverseBits(n)
print(bin(n))
print(bin(r))
assert(r == 3221225471)