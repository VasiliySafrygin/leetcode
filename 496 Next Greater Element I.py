from typing import List
from collections import deque  


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_nums = dict()
        stack = []
        for n in reversed(nums2):
            while stack and n >= stack[-1]:
                stack.pop()
            next_greater_nums[n] = stack[-1] if stack else -1
            stack.append(n)
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            res[i] = next_greater_nums[nums1[i]]
        return res

s = Solution()

r = s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
print(r)
assert(r == [-1,3,-1])