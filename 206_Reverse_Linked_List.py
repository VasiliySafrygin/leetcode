"""
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
from typing import Optional


def print_linked_list(list_node):
    values = []
    while list_node:
        values.append(list_node.val)
        list_node = list_node.next
    print('->'.join(map(lambda x: str(x), values)))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        _prev, _cur, _next = None, head, None

        while _cur:
            _next = _cur.next
            _cur.next = _prev
            _prev = _cur
            _cur = _next

        return _prev


if __name__ == '__main__':
    s = Solution()

    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    r = s.reverseList(nodes)
    print_linked_list(r)
