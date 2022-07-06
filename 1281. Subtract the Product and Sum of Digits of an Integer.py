class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n > 0:
            tail = n % 10
            product *= tail
            sum += tail
            n = n // 10
        return product - sum


s = Solution()

r = s.subtractProductAndSum(234)
print(r)
assert(r == 15)


r = s.subtractProductAndSum(1)
print(r)
assert(r == 0)

r = s.subtractProductAndSum(4)
print(r)
assert(r == 0)

r = s.subtractProductAndSum(10)
print(r)
assert(r == -1)

r = s.subtractProductAndSum(4421)
print(r)
assert(r == 21)
