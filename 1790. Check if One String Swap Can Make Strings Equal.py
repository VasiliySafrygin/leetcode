class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0 
        different = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                different.append([s1[i], s2[i]])
                cnt += 1
            if cnt > 2: 
                return False
        
        if cnt== 0 or (cnt == 2 and different[0] == list(reversed(different[1]))):
            return True
        return False
        
s = Solution()
print(s.areAlmostEqual('aa', 'bb'))
print(s.areAlmostEqual('relb', 'relb'))
print(s.areAlmostEqual('abb', 'bba'))
