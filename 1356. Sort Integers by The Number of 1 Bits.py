from typing import List

def count_bits(value) -> int:
    cnt = 0
    while value:
        cnt += value & 1
        value >>= 1
    return (cnt, value)


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=count_bits)


s = Solution()

r = s.sortByBits([0,1,2,3,4,5,6,7,8])
print(r)
assert(r == [0,1,2,4,8,3,5,6,7])


r = s.sortByBits([1,2,4,8,16,32,64,128,256,512,1024])
print(r)
assert(r == [1,2,4,8,16,32,64,128,256,512,1024])


r = s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
print(r)
assert(r == [1024,512,256,128,64,32,16,8,4,2,1])
