from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter([s for s in s1])
        n1 = len(s1)
        for i in range(len(s2) - len(s1) + 1):
            if Counter([s for s in s2[i:i+n1]]) == cnt1:
                return True
        return False

s = Solution()

r = s.checkInclusion("hello", "ooolleoooleh")
print(r)
assert(r == False)


r = s.checkInclusion("adc", "dcda")
print(r)
assert(r == True)

r = s.checkInclusion("ab", "eidbaooo")
print(r)
assert(r == True)

r = s.checkInclusion("ab", "eidboaoo")
print(r)
assert(r == False)