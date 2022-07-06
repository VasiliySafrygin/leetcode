from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height) - 1
        _max = 0
        while s < e:
            _max = max(_max, min(height[s], height[e]) * (e - s))
            if height[s] > height[e]:
                e -= 1
            else:
                s += 1
        return _max

s = Solution()
r = s.maxArea([1,8,6,2,5,4,8,3,7])
print(r)
assert(r == 49)

r = s.maxArea([1,1])
print(r)
assert(r == 1)