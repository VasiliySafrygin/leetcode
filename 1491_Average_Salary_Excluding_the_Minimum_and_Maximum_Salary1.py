import math
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        print(salary, salary[1:-1])
        return sum(salary[1:-1]) / (len(salary) - 2)


s = Solution()
r = s.average([4000,3000,1000,2000])

print(r)
