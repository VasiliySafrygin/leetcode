from re import template


class Solution:
    def interpret(self, command: str) -> str:
        result = []
        if len(command) == 1 and command[0] == 'G':
            return 'G'
        i = 0
        while i < len(command) - 1:
            if command[i:i+2].startswith('G'):
                result.append('G')
                i += 1
            if command[i:i+2].startswith('()'):
                result.append('o')
                i += 2
            if command[i:i+2].startswith('(a'):
                result.append('al')
                i += 4
        
        if i < len(command) and command[i] == 'G':
            result.append('G')

        return ''.join(result)


s = Solution()
r = s.interpret("G()(al)")
print(r)
assert(r == "Goal")

r = s.interpret("G()(al)GG")
print(r)
assert(r == "GoalGG")

r = s.interpret("G()()()()(al)")
print(r)
assert(r == "Gooooal")

r = s.interpret("(al)G(al)()()G")
print(r)
assert(r == "alGalooG")
