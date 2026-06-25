# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pn = []
        self.qn = []
        def traverse(root, nodes):
            if not root:
                nodes.append(None)
                return
            traverse(root.left,nodes)
            traverse(root.right,nodes)
            nodes.append(root.val)
        traverse(q, self.qn)
        traverse(p,self.pn)
        return self.pn == self.qn