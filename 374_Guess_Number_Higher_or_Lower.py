# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

GUESS_NUMBER = 5

def guess(num: int) -> int:
    if num > GUESS_NUMBER:
        return -1
    elif num < GUESS_NUMBER:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if guess(mid) == 1:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif guess(mid) == -1:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return -1

s = Solution()

r = s.guessNumber(30)
print(r)