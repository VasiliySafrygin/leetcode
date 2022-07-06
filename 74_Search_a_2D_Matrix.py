from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix) 
        n = len(matrix[0])
        high = m * n - 1
        if high == 0: 
            return  matrix[0][0] == target

        while low <= high:
            mid = (low + high) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid -1
        return False

s = Solution()
# r = s.searchMatrix([[1,2,3]], target = 4)
# r = s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
r = s.searchMatrix([[1]], target = 1)
print(r)
assert(r == True)
