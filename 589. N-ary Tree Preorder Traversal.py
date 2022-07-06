# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    
    def __repr__(self) -> str:
        return str(self.val)

from typing import List


class Solution:
    def get_children(self, node: Node) -> List[Node]:
        children = [node]
        if not node.children:
            return children
        
        for child in node.children:
            children.extend(self.get_children(child))
        return children

    def preorder(self, root: Node) -> List[int]:
        if root is None:
            return []
        return [i.val for i in self.get_children(root)]


n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n5, n6])
n2 = Node(2)
n1 = Node(1, [n3, n2, n4])

s = Solution()

r = s.preorder(n1)
print(r)
assert(r == [1,3,5,6,2,4])
