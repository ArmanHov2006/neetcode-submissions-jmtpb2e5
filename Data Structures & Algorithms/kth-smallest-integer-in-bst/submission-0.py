# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is not None:    
            count = self.elementCount(root.left)
            if count == k-1:
                return root.val
            elif count > k-1:
                return self.kthSmallest(root.left,k)
            else:
                return self.kthSmallest(root.right, k - count - 1)

    def elementCount(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.elementCount(root.right) + self.elementCount(root.left)