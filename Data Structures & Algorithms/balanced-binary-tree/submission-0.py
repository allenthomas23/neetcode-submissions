# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(root):

            if not root:
                return 0

            maxl,maxr=0,0
            maxl = height(root.left)
            maxr = height(root.right)
            if abs(maxl- maxr) >1:
                self.balanced = False
            return 1+ max(maxl,maxr) 
        height(root)
        return self.balanced