from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        step = (arr[-1] - arr[0]) / (len(arr) - 1)
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != step:
                return False
        return True


s = Solution()

r = s.canMakeArithmeticProgression([3,5,1,0])
print(r)

assert(r == False)
