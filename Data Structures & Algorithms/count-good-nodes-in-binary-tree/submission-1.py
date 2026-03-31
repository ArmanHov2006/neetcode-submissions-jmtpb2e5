# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, float("-inf"))

    def count(self, root, m) -> int:
        
        if not root:
            return 0
        return (
        (1 if root.val >= m else 0)
        + self.count(root.left, max(m, root.val))
        + self.count(root.right, max(m, root.val))
    )