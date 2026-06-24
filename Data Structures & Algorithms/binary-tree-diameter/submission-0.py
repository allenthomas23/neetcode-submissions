# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def height(root):
            if not root:
                return 0
            maxl,maxr =0,0
            maxl += height(root.left)
            maxr += height(root.right)
            self.res = max(self.res,maxl+maxr)
            return 1 + max(maxl, maxr)

        height = height(root)
        return self.res