class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1
        while i >= 0:
            c = s[i]
            if c == '#':
                result.append(chr(int(s[i-2:i]) + 96))
                i -= 3
            else:
                result.append(chr(int(s[i]) + 96))
                i -= 1
        return ''.join(reversed(result))

#96
s = Solution()
r = s.freqAlphabets('10#11#12')
print(r)
assert(r == 'jkab')


r = s.freqAlphabets('1326#')
print(r)
assert(r == 'acz')