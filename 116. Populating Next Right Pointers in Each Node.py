# Definition for a Node.
import queue
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    
    def __repr__(self):
        return f"{self.val}"


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        s = queue.deque([root, None])
        _prev = None
        while len(s) > 1:
            n = s.popleft()
            if n is None:
                s.append(None)
            else:
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)
            if _prev:
                _prev.next = n
            _prev = n
        return root


s = Solution()
r = s.connect(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7))))
pass
            
        