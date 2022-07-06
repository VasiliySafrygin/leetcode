from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ptr1 = 0
        # ptr2 = 0
        # cnt1 = 0
        # cnt2 = 0
        # while ptr2 < len(nums):
        #     if nums[ptr2] == 0:
        #         nums[ptr1] = 0
        #         ptr1 +=1
        #     elif nums[ptr2] == 1:
        #         cnt1 += 1
        #     elif nums[ptr2] == 2:
        #         cnt2 += 1    
        #     ptr2 += 1
        # for _ in range(cnt1):
        #     nums[ptr1] = 1
        #     ptr1 += 1
        # for _ in range(cnt2):
        #     nums[ptr1] = 2
        #     ptr1 += 1
        if(nums==[]):return
        start=0
        end=len(nums)-1
        i=0
        while(i<=end):
            if(nums[i]==2):
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
            elif(nums[i]==0):
                nums[i],nums[start]=nums[start],nums[i]
                start+=1
                i+=1
            else:
                i+=1

s = Solution()
nums = [2,0,2,1,1,0]
s.sortColors(nums)
assert(nums == [0,0,1,1,2,2])
pass