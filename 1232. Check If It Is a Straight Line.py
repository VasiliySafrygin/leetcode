from cmath import inf
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2: 
            return True

        try:
            step = (coordinates[0][0] - coordinates[1][0]) / (coordinates[0][1] - coordinates[1][1])
        except:
            step = inf
            
        for i in range(1, len(coordinates) - 1):
            try:
                step_i = (coordinates[i][0] - coordinates[i + 1][0]) / (coordinates[i][1] - coordinates[i + 1][1])
            except:
                step_i = inf
            if step_i != step:
                return False
        return True

s = Solution()

r = s.checkStraightLine([[1,-8],[2,-3],[1,2]])
print(r)
assert(r == False)

r = s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
print(r)
assert(r == True)

r = s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
print(r)
assert(r == False)

r = s.checkStraightLine([[2,4],[2,5],[2,8]])
print(r)
assert(r == True)

r = s.checkStraightLine([[0,0],[0,1],[0,-1]])
print(r)
assert(r == True)