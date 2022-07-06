from curses.ascii import SO
from typing import List


class Solution:
    def reverseString(self, s: str) -> str:
        head = 0
        tail = len(s) - 1 
        str_arr = [None] * len(s)

        for _ in range(len(s) // 2 + 1):
            str_arr[head], str_arr[tail] = s[tail], s[head]
            head += 1
            tail -= 1
        
        return ''.join(str_arr)

    def reverseWords(self, s: str) -> str:
        word_arr = []
        for word in s.split(' '):
            word_arr.append(self.reverseString(word))
        return ' '.join(word_arr)


s = Solution()

r = s.reverseWords("Let's take LeetCode contest")
print(r)
assert(r == "s'teL ekat edoCteeL tsetnoc")


r = s.reverseWords("b")
print(r)
assert(r == "b")
