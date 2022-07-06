# Definition for singly-linked list.
import heapq
from typing import List, Optional


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
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = result_list = ListNode()
        has_next = True
        while has_next:
            has_next = False
            _min_val = None
            _min_idx = None
            for i in range(0, len(lists)):
                if lists[i] and _min_val is None:
                    _min_val = lists[i].val
                    _min_idx = i
                    has_next = True
                if lists[i] and lists[i].val < _min_val:
                    _min_val = lists[i].val
                    _min_idx = i
                    has_next = True
            if has_next:
                result_list.next = ListNode(_min_val)
                result_list = result_list.next
                lists[_min_idx] = lists[_min_idx].next
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = result_list = ListNode()
        q = [] 
        for i in lists:
            while i:
                heapq.heappush(q, i.val)
                i = i.next
        while q:
            result_list.next = ListNode(heapq.heappop(q))
            result_list = result_list.next    
        return head.next    

s = Solution()


# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

l = s.mergeKLists([l1, l2, l3])
print_linked_list(l)