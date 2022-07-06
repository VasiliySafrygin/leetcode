from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product_without_zeros = 1
        if len(nums) in [0, 1]:
            return nums

        for n in nums:
            if n != 0:
                product_without_zeros *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0 for _ in range(len(nums))]
        elif zero_cnt == 1:
            return [0 if n!=0 else product_without_zeros for n in nums]
        else:
            return [int(product_without_zeros / n) if n!=0 else product_without_zeros for n in nums]


s = Solution()
r = s.productExceptSelf([1,2,3,4])
print(r)
assert(r == [24,12,8,6])

r = s.productExceptSelf([-1,1,0,-3,3])
print(r)
assert(r == [0,0,9,0,0])
