from typing import List
from unittest import result


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(0, len(nums) -1, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]

        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]

        return result


s = Solution()

r  = s.singleNumber([2,2,1])
print(r)
assert(r == 1)


r  = s.singleNumber([4,2,2,1,1])
print(r)
assert(r == 4)

