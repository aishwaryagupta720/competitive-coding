# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return node
        if node.val>p.val and node.val>q.val:
            temp = self.lowestCommonAncestor(node.left,p,q)
        elif node.val<p.val and node.val<q.val:
            temp = self.lowestCommonAncestor(node.right,p,q)
        else:
            temp=node
        return temp
            