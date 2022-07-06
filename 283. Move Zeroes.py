from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_pos = 0
        for num in nums:
            if num != 0:
                nums[new_pos] = num
                new_pos += 1
        for i in range(new_pos, len(nums)):
            nums[i] = 0
        

s = Solution()
n = [1,2,0,3,4,0,5,0]

s.moveZeroes(n)

assert(n == [1,2,3,4,5,0,0,0])
