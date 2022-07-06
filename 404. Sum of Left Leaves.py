# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def sum_left(self, root: Optional[TreeNode], _sum=0, _use_val=False) -> int:
        if not root:
            return _sum
    
        l = self.sum_left(root.left, _sum, True)
        r = self.sum_left(root.right, _sum, False)
        if _use_val and not root.left and not root.right:
            return root.val + _sum
        else:
            return _sum + l + r
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sum_left(root)


s = Solution()

# r = s.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
# print(r)
# assert(r == 24)

r = s.sumOfLeftLeaves(TreeNode(1, TreeNode(2, TreeNode(4, None)), TreeNode(3, None, TreeNode(5))))
print(r)
assert(r == 24)