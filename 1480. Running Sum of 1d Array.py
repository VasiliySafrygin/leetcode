"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for n in nums:
            sum += n
            result.append(sum)
        return result


s = Solution()
r = s.runningSum([1,2,3,4])
assert(r == [1,3,6,10])

r = s.runningSum([1,1,1,1,1])
assert(r == [1,2,3,4,5])


r = s.runningSum([3,1,2,10,1])
assert(r == [3,4,6,16,17])
