from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return low 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

s = Solution()
r = s.searchInsert([1,3,5,6], 5)
print(r)
assert(r == 2)


r = s.searchInsert([1,3,5,6], 2)
print(r)
assert(r == 1)

r = s.searchInsert([1,3,5,6], 7)
print(r)
assert(r == 4)

r = s.searchInsert([2,3,5,6], 1)
print(r)
assert(r == 0)