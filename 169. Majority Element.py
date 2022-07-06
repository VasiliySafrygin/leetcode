from typing import Dict, List, Tuple, Optional


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt: Dict[int, int] = dict()
        _max: Tuple[int, Optional[int]] = (0, None)
        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
            _max = max(_max, (cnt[n], n))
        return _max[1]

s = Solution()
r = s.majorityElement([2,2,1,1,1,2,2])
print(r)
assert(r == 2)