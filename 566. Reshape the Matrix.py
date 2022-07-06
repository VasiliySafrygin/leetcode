from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        result_mat = [[None for i in range(c)] for _ in range(r)]
        for p in range(m * n):
            i = p // n
            j = p % n
            ri = p // c
            rj  = p % c
            result_mat[ri][rj] = mat[i][j]
        return result_mat

s = Solution()
# r = s.matrixReshape([[1,2],[3,4]], 1, 4)
# print(r)
# assert(r == [[1,2,3,4]])

r = s.matrixReshape([[1,2],[3,4]], 4, 1)
print(r)
assert(r == [[1],[2],[3],[4]])