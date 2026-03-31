# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            r = preorder[0]
            root = TreeNode(r)
            l_i, r_i = inorder[:inorder.index(r)], inorder[inorder.index(r) + 1:]
            l_len, r_len = len(l_i), len(r_i)
            l_p, r_p = preorder[1:l_len+1], preorder[l_len+1:]
            root.left = self.buildTree(l_p, l_i)
            root.right = self.buildTree(r_p, r_i)
            return root
            