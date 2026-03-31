from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

            if level:
                res.append(level[-1])

        return res
