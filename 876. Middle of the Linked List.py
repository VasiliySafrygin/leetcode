# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val)
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_ptr = head
        slow_prt = head

        while fast_ptr:
            try:
                fast_ptr = fast_ptr.next.next
            except AttributeError:
                break
            slow_prt = slow_prt.next
        return slow_prt

s = Solution()

r = s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))) 
print(r)
assert(r.val == 3)

r = s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
print(r)
assert(r.val == 4)

