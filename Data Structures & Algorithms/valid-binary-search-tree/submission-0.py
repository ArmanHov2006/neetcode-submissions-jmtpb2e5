# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.iVT(root)

    def iVT(self, root, min= float("-inf"), max = float("inf")):
        if root is None:
            return True
        l = self.iVT(root.left, min, root.val)
        r = self.iVT(root.right, root.val, max)
        return min < root.val < max and l and r