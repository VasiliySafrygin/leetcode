from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = []
        cnt_s = Counter(s)
        for c in iter(t):
            cnt_s[c] -= 1
        for k, v in cnt_s.items():
            if v < 0:
                result.append(k)
        return ''.join(result)
        
        

s = Solution()
r = s.findTheDifference("abcd", "abcde")
print(r)
assert(r == "e")


r = s.findTheDifference("a", "aa")
print(r)
assert(r == "a")