# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val)
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = head
        n_ptr = head
        ptr = head
        for _ in range(n):
            try:
                n_ptr = n_ptr.next
            except AttributeError:
                return None
        if not n_ptr:
            return result.next

        while n_ptr.next:
            n_ptr = n_ptr.next
            ptr = ptr.next
        
        try:
            ptr.next = ptr.next.next
        except AttributeError:
            ptr.next = None
        return result


s = Solution()
r = s.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
print(r)

r = s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2) 
print(r)


r = s.removeNthFromEnd(ListNode(1), 1) 
print(r)

r = s.removeNthFromEnd(ListNode(1, ListNode(2)), 1) 
print(r)
