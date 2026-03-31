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
        if root.val >= m:
            m = root.val
            return 1 + self.count(root.left, m) + self.count(root.right, m)
        else:
            return self.count(root.left, m) + self.count(root.right, m)