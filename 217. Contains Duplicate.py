from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = dict()
        for n in nums:
            if n in cnt:
                return True
            else:
                cnt[n] = 1
        return False


s = Solution()
r = s.containsDuplicate([1,2,3,1])
assert(r == True)