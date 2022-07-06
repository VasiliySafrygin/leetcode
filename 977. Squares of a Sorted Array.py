from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        i = 0
        j = n - 1
        _sorted_squares = [None] * n
        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                _sorted_squares[k] = nums[i] ** 2
                i += 1
            else:
                _sorted_squares[k] = nums[j] ** 2
                j -= 1
        return _sorted_squares
                

s = Solution()

r = s.sortedSquares([-4,-1,0,3,10])
print(r)
assert(r == [0,1,9,16,100])


r = s.sortedSquares([-7,-3,2,3,11])
print(r)
assert(r == [4,9,9,49,121])



# int n = A.size(), i = 0, j = n - 1;
#         vector<int> res(n);
#         for (int k = n - 1; k >= 0; --k) {
#             if (abs(A[i]) > abs(A[j])) {
#                 res[k] = A[i] * A[i];
#                 ++i;
#             } else {
#                 res[k] = A[j] * A[j];
#                 --j;
#             }
#         }
#         return res;