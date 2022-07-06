# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        while head:
            sum <<= 1
            sum |= head.val
            head = head.next
        return sum


s = Solution()
r = s.getDecimalValue(ListNode(1, ListNode(0, ListNode(1))))
print(r)
assert(r == 5)