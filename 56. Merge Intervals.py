from typing import List
import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [[None, None]]
        heap = []
        if len(intervals) < 2:
            return intervals
        for i in intervals:
            heapq.heappush(heap, (i[0], 0))
            heapq.heappush(heap, (i[1], 1))
        cnt = 0
        while len(heap):
            item = heapq.heappop(heap)
            # print(item, cnt)
            if item[1] == 0:
                if result[-1][0] is None:
                    result[-1][0] = item[0]
                cnt += 1
            elif item[1] == 1:
                cnt -= 1
                if cnt == 0:
                    result[-1][1] = item[0]
                    result.append([None, None])

        return result[:-1]


s = Solution()

# r = s.merge([[1,3],[2,6],[8,10],[15,18]])
# print(r)
# assert(r == [[1,6],[8,10],[15,18]])


# r = s.merge([[1,3],[2,4],[3,6],[8,10],[15,18]])
# print(r)
# assert(r == [[1,6],[8,10],[15,18]])


r = s.merge([[1,4],[4,5]])
print(r)
assert(r == [[1,5]])

