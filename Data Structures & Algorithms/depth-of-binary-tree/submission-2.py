# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxd = 0
        s = list()
        s.append((root,1))
        while s:
            node,d = s.pop()
            if node.right:
                s.append((node.right,d+1))
            if node.left:
                s.append((node.left,d+1))
            maxd = max(d,maxd)
        return maxd
