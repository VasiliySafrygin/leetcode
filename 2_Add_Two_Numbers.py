# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        head = ListNode()
        c = head
        
        add = 0
        
        while a or b or add:
            try:
                a_val = a.val
            except AttributeError:
                a_val = 0
            
            try:
                b_val = b.val
            except AttributeError:
                b_val = 0
                
            c.val = (add + a_val + b_val) % 10
            
            add = (add + a_val + b_val) // 10
            
            try:
                a = a.next
            except AttributeError:
                pass
            
            try:
                b = b.next
            except AttributeError:
                pass
            
            if a or b or add:
                c.next = ListNode()
                c = c.next
                    
        return head