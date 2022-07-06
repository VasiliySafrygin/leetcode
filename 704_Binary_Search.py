from typing import List


class Solution:
    def binary_search_recursive(self, nums: List[int], target: int, low: int, high: int):
        # Check base case
        if high >= low:
            mid = (high + low) // 2
    
            # If element is present at the middle itself
            if nums[mid] == target:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif nums[mid] > target:
                return self.binary_search_recursive(nums, target, low, mid - 1)
    
            # Else the element can only be present in right subarray
            else:
                return self.binary_search_recursive(nums, target, mid + 1, high)

        else:
            # Element is not present in the array
            return -1

    def binary_search_iterative(self, nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        mid = 0
    
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
                return nums[mid]
    
        # If we reach here, then the element was not present
        return nums[mid]

    def search(self, nums: List[int], target: int) -> int:
        # return self.binary_search_recursive(nums, target, 0, len(nums) - 1)
        return self.binary_search_iterative(nums, target)


s = Solution()

r = s.search([-1,0,3,5,9,12], 4)

print(r)
