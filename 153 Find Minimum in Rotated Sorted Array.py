from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            _min = nums[-1]
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > _min:
                low = mid + 1
            elif nums[mid] <= _min:
                _min = nums[mid]
                high = mid - 1
        return _min


s = Solution()

# r = s.findMin([3])
# print(r)
# assert(r == 3)

r = s.findMin([2, 1])
print(r)
assert(r == 1)

# r = s.findMin([3,4,5,1,2])
# print(r)
# assert(r == 1)  

# r = s.findMin([4,5,6,7,0,1,2])
# print(r)
# assert(r == 0)  

# r = s.findMin([11,13,15,17])
# print(r)
# assert(r == 11)