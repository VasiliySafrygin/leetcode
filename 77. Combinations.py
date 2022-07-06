import queue
from typing import List

# class Solution {
# public:
# 	vector<vector<int>> combine(int n, int k) {
# 		vector<vector<int>> res;
# 		vector<int> temp(k, 0);
# 		int i = 0;
# 		while (i >= 0)
# 		{
# 			temp[i]++;
# 			if (temp[i] > n)
# 				i--;
# 			else if (i == k - 1)
# 				res.push_back(temp);
# 			else
# 			{
# 				i++;
# 				temp[i] = temp[i - 1];
# 			}
# 		}
# 		return res;
# 	}
# };
class Solution:
    def dfs(self, result: List[List[int]], temp:List[int], index: int, n: int, k: int):
        for i in range(index + 1, n + 1):
            temp.append(i)
            if len(temp) == k:
                result.append(temp.copy())
                temp.pop()
                return 
            else:
                self.dfs(result, temp, i, n, k)
                temp.pop()
                
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [[]];
        temp = [];
        self.dfs(result, temp, 0, n, k)
        return result
        

s = Solution()

r = s.combine(4, 2)
print(r)