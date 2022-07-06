from typing import List


class Solution:
    def bin_serach(self, nums: List[int], target: int) -> bool:
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = (e + s) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for l in matrix:
        #     if self.bin_serach(l, target):
        #         return True
        # return False

        # if (matrix.empty() || matrix[0].empty()) return false;
        
        # int i = matrix.size() - 1;
        # int j = 0;
        
        # while (i >= 0 && j < matrix[0].size()){
        #     if (matrix[i][j] == target) return true;
        #     else if (matrix[i][j] < target) j++;
        #     else if (matrix[i][j] > target) i--;
        # }
        # return false;

        if not len(matrix):
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i <= m - 1 and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                 i += 1
            elif matrix[i][j] > target:
                 j -= 1
        return False


s = Solution()
r = s.searchMatrix(matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 7)
print(r)
assert(r == True)

r = s.searchMatrix(matrix=[[-5], [6]], target = 6)
print(r)
assert(r == True)


r = s.searchMatrix(matrix=[[-5, 6]], target = 6)
print(r)
assert(r == True)

r = s.searchMatrix(matrix=[[-5]], target = -5)
print(r)
assert(r == True)
