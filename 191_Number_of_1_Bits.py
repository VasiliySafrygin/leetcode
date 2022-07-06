class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0        
        while(n != 0):
            n = n & (n - 1)
            cnt += 1
        return cnt



s = Solution()


r = s.hammingWeight(0b00000000000000000000000000001011)
assert (r == 3)
print(r)


r = s.hammingWeight(0b00000000000000000000000010000000)
assert (r == 1)
print(r)


r = s.hammingWeight(0b11111111111111111111111111111101)
assert (r == 31)
print(r)


r = s.hammingWeight(0b00000000000000000000000000000001)
assert (r == 1)
print(r)


r = s.hammingWeight(0b00000000000000000000000000000000)
assert (r == 0)
print(r)
