# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f'{self.val}'
        
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        result = ListNode()

        ptr1 = head
        ptr2 = head.next
        while ptr2:
            if ptr1.val != ptr2.val:
                result.next = ptr1
                ptr1, ptr2 = ptr2, ptr2.next
            elif ptr1.val == ptr2.val:
                while ptr1 and ptr1.val != ptr2.val:
                    ptr1 = ptr1.next
                if ptr1:
                    ptr2 = ptr1.next
                else:
                    ptr2 = None

