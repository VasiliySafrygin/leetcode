"""
public class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
}
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (s + e) // 2
            if nums[mid] > nums[mid + 1]:
                e = mid
            else:
                s = mid + 1
        return s

s = Solution()
r = s.findPeakElement([1,2,3,4,2,5,4])
print(r)