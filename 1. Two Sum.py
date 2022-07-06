from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d = dict()
        # for i, n in enumerate(nums):
        #     if target - n in d:
        #         return sorted([i, d[target - n]])
        #     d[n] = i
        _nums = sorted([(k, i) for i, k in enumerate(nums)])
        head_ptr = 0
        tail_ptr = len(_nums) - 1
        while head_ptr < tail_ptr:
            if _nums[head_ptr][0] + _nums[tail_ptr][0] == target:
                return [_nums[head_ptr][1], _nums[tail_ptr][1]]
            elif _nums[head_ptr][0] + _nums[tail_ptr][0] > target:
                tail_ptr -= 1
            else:
                head_ptr += 1


s  = Solution()
r = s.twoSum([2,7,11,15], target = 9)
print(r)
assert(r == [0,1])

r = s.twoSum([3,2,4], target = 6)
print(r)
assert(r == [1,2])
        