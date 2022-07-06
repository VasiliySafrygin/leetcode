# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

        
class Solution:
    def countDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        depth += 1
        return max(
            self.countDepth(root.left, depth), 
            self.countDepth(root.right, depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.countDepth(root)


s = Solution()

r = s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(r)
assert(r == 3)