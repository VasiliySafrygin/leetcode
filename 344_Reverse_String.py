from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s) - 1 
        for _ in range(len(s) // 2):
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1


s = Solution()
ss = ["h","e","l","l","o"]
s.reverseString(ss)
print(ss)
assert(ss == ["o","l","l","e","h"])


ss = ["o"]
s.reverseString(ss)
print(ss)
assert(ss == ["o"])


ss = ["o", "o"]
s.reverseString(ss)
print(ss)
assert(ss == ["o", "o"])
