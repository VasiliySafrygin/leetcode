from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat) - 1 
        j = 0
        sum = 0
        while j <= n:
            if j != (n - j):
                sum += mat[j][j] + mat[j][n - j]
            else:
                sum += mat[j][j]
            j += 1
        return sum

s = Solution()

r = s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
print(r)
assert(r == 25)

r = s.diagonalSum([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])
print(r)
assert(r == 68)
