from unittest import result


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = iter(word1)
        ptr2 = iter(word2)
        result = []
        c1 = next(ptr1)
        c2 = next(ptr2)
        while c1 or c2:
            result.append(c1)
            result.append(c2)
            try:
                c1 = next(ptr1)
            except StopIteration:
                c1 = ''
            try:
                c2 = next(ptr2)
            except StopIteration:
                c2 = ''

        return ''.join(result)



s = Solution()
r = s.mergeAlternately("abc", "pqr")
print(r)
assert(r == "apbqcr")

r = s.mergeAlternately("ab", "pqrs")
print(r)
assert(r == "apbqrs")