# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        queue=[[root]]
        level=1
        for nodes in queue:
            nodelist=[]
            for node in nodes:
                if node.left:
                    nodelist.append(node.left)
                if node.right:
                    nodelist.append(node.right)
            if len(nodelist)>0:
                queue.append(nodelist)
        return len(queue)
            