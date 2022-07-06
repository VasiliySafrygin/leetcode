from typing import List

def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k - 1)
        reverse(nums, k,  len(nums)-1)

    def rotate(self, nums: List[int], k: int) -> None:
        _tmp = nums[0]
        n = len(nums)
        i = 0
        for _ in range(len(nums)):
            new_index = (i + k) % n
            _tmp, nums[new_index] = nums[new_index], _tmp
            # nums[new_index] = nums[i]

            i = new_index


s = Solution()

# n = [1,2,3,4,5,6,7,8,9]
n = [-1,-100,3,99]
s.rotate(n, 2)
print(n)
# assert(n == [9,1,2,3,4,5,6,7,8])
assert(n == [3,99,-1,-100])


# r = s.rotate([1,2,3,4,5,6,7,8,9], 2)
# print(r)
# assert(r == [8,9,1,2,3,4,5,6,7])

# r = s.rotate([1,2,3,4,5,6,7,8,9], 2)
# print(r)
# assert(r == [8,9,1,2,3,4,5,6,7])