from typing import List

# c++ version
# class Solution {
# public:
#     int rob(vector<int>& nums) {
#         int n=nums.size();
#         if(!n) return 0;
#         if(n==1) return nums[0];
#         vector<int> dp={nums[0],max(nums[0],nums[1])};
#         for(int i=2;i<n;++i)
#             dp.push_back(max(nums[i]+dp[i-2],dp[i-1]));
#         return dp.back();
#     }
# };

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: 
            return 0
        if n == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
        return dp[-1]


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

s = Solution()
r = s.rob([1,2,3,1])
print(r)
assert(r)

r = s.rob([2,7,9,3,1])
print(r)
assert(r == 12)