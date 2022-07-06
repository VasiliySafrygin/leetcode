from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] = min(
                    triangle[row][col] + triangle[row + 1][col], 
                    triangle[row][col] + triangle[row + 1][col + 1])
        return triangle[0][0]


s = Solution()
r = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(r)
assert(r == 11)
 
r = s.minimumTotal([[2]])
print(r)
assert(r == 2)

r = s.minimumTotal([[2], [2, 4]])
print(r)
assert(r == 4)