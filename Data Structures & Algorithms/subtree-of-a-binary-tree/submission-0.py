# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def same(q,p):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val !=p.val:
                return False
            return same(q.left,p.left) and same(q.right,p.right)



        if not root:
            return False

        return same(root,subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)