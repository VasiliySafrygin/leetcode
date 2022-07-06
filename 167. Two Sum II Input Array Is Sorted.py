from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head_pointer = 0
        tail_pointer = len(numbers) - 1
        while head_pointer < tail_pointer:
            if numbers[head_pointer] + numbers[tail_pointer] == target:
                return [head_pointer + 1, tail_pointer + 1]
            elif numbers[head_pointer] + numbers[tail_pointer] > target:
                tail_pointer -= 1
            else:
                head_pointer += 1
        raise Exception('Not found')


s = Solution()

r = s.twoSum([2,7,11,15], target = 9)
print(r)
assert(r == [1,2])
