# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.queue = deque()
        self.queue.append(root)
        self.res = []

        while self.queue:
            nodes = []
            for i in range(len(self.queue)):
                node = self.queue.popleft()
                nodes.append(node.val)
                if node.left:
                    self.queue.append(node.left) 
                if node.right:
                    self.queue.append(node.right)
            self.res.append(nodes)
        return self.res
            
            
