from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # s = 0
        # e = len(nums) - 1
        
        # while s <= e:
        #     mid = (s + e) // 2
        #     n = nums[mid]
        #     if n == target:
        #         s = e = mid
        #         break
        #     elif n > target:
        #         e -= 1
        #     else:
        #         s += 1
        # else:
        #     return [-1, -1]  # not found target
        
        # while (nums[s] == target or nums[e] == target):
        #     if s-1 >=0 and nums[s-1] == target:
        #         s -=1
        #     if e+1 < len(nums) and nums[e + 1] == target:
        #         e +=1
        # return [s, e] 
        range_start = -1    
        range_end = -1    
        
        if (nums == None or len(nums) == 0):
            return [range_start, range_end]
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            range_end = end
        elif nums[start] == target:
            range_end = start
            
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid
                
        if nums[start] == target:
            range_start = start
        elif nums[end] == target:
            range_start = end            
        
        return [range_start, range_end]
        
s = Solution()

r = s.searchRange([1,1], target = 1)
print(r)
assert(r == [0,1])

r = s.searchRange([5,7,7,8,8,10], target = 8)
print(r)
assert(r == [3,4])


r = s.searchRange([5,7,7,8,8,10], target = 6)
print(r)
assert(r == [-1,-1])

r = s.searchRange([], target = 0)
print(r)
assert(r == [-1,-1])