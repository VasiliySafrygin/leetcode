from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        _min = (-1, -1)
        for i, [x2, y2] in enumerate(points):
            if x2 == x or y2 == y:
                distance = (abs(x - x2) + abs(y - y2), i)
                if _min == (-1, -1):
                    _min = distance
                else:
                    _min = min(_min, distance)
        return _min[1]

s = Solution()

r = s.nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])
print(r)
assert(r == 2)
