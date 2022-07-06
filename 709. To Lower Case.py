class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for c in iter(s):
            code = ord(c)
            if 64 < code < 91:
                code += 32
            result.append(chr(code))
        return ''.join(result)

s = Solution()
