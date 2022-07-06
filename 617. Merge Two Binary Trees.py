# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def merge(self, root1, root2):
        if root1 and root2:
            return TreeNode(
                val=root1.val + root2.val, 
                left=self.merge(root1.left, root2.left),
                right=self.merge(root1.right, root2.right))
        elif root1 and not root2:
            return TreeNode(
                val=root1.val, 
                left=self.merge(root1.left, None),
                right=self.merge(root1.right, None))
        elif not root1 and root2:
            return TreeNode(
                val=root2.val, 
                left=self.merge(None, root2.left),
                right=self.merge(None, root2.right))
        else:
            return

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1, root2)

s = Solution()
root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, right=TreeNode(4)), TreeNode(3, right=TreeNode(7)))
r = s.merge(root1, root2)
pass