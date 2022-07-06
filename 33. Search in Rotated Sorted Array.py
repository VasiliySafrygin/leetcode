from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _min = min(nums)
        _min_index = nums.index(_min)
        low = 0
        high = len(nums) - 1
        if target < nums[-1]:
            low = _min_index
        elif target > nums[-1]:
            high = _min_index
        else:
            return len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1
        return -1

s = Solution()

r = s.search([4,5,6,7,0,1,2], 0)
print(r)
assert(r == 4)


r = s.search([4,5,6,7,0,1,2], 3)
print(r)
assert(r == -1)


r = s.search([4,5,6,7,0,1,2], 7)
print(r)
assert(r == 3)