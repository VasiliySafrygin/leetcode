from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target

        _min = min(nums)
        _min_index = nums.index(_min)
        low = 0
        high = len(nums) - 1
        while high > 0 and nums[low] == nums[high]:
            high -= 1

        if target < nums[high]:
            low = _min_index
        elif target > nums[high]:
            high = _min_index
        else:
            return True
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1
        return False

s = Solution()

r = s.search([2,2,2,3,2,2,2], 3)
print(r)
assert(r == True)

r = s.search(nums = [2,5,6,0,0,1,2], target = 0)
print(r)
assert(r == True)

r = s.search(nums = [2,5,6,0,0,1,2], target = 3)
print(r)
assert(r == False)


r = s.search(nums = [0], target = 0)
print(r)
assert(r == True)

r = s.search(nums = [2], target = 3)
print(r)
assert(r == False)
