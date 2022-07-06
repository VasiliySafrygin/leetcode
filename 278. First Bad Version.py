BAD_VER = 1

def isBadVersion(n: int) -> bool:
    if n >= BAD_VER:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = 1
        if isBadVersion(1):
            return 1

        while low < high:
    
            mid = (high + low) // 2
    
            if not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            
            elif not isBadVersion(mid):
                low = mid #+ 1
    
            elif isBadVersion(mid):
                high = mid #- 1
    
            else:
                return mid
    
        return mid

s = Solution()

# BAD_VER = 1
# r = s.firstBadVersion(3)
# print(r)
# assert(r == BAD_VER)

# BAD_VER = 4
# r = s.firstBadVersion(5)
# print(r)
# assert(r == BAD_VER)


# BAD_VER = 6
# r = s.firstBadVersion(6)
# print(r)
# assert(r == BAD_VER)


# BAD_VER = 3
# r = s.firstBadVersion(7)
# print(r)
# assert(r == BAD_VER)


BAD_VER =1150769282
r = s.firstBadVersion(1420736637)
print(r)
assert(r == BAD_VER)
