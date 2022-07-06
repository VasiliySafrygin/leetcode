from typing import List
import heapq

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _sums = []
        for l in accounts:
            heapq.heappush(_sums, -1 * sum(l))
        return heapq.heappop(_sums) * -1


s = Solution()
r = s.maximumWealth([[1,2,3],[3,2,1]])
print(r)
assert(r == 6)

r = s.maximumWealth([[1,5],[7,3],[3,5]])
print(r)
assert(r == 10)

r = s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
print(r)
assert(r == 17)


