# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = result = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else: 
                result.next = list2
                list2 = list2.next
            
            result = result.next
        
        if list1:
            result.next = list1
        if list2:
            result.next = list2
        return head.next

s = Solution()

r = s.mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))),
    ListNode(1, ListNode(3, ListNode(4))),
)


pass

r = s.mergeTwoLists(
    None,
    ListNode(0),
)

pass