# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        ptr1 = ptr2 = head
        
        while ptr1 or ptr2:
             
            ptr1 = ptr1.next
            try:
                ptr2 = ptr2.next.next
            except AttributeError:
                break
            
            if ptr2 is ptr1:
                return True

        return False

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
# d.next = b

r = s.hasCycle(a)
print(r)
