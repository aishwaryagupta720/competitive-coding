# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==[]:
            return []
        def traverse(node):
            if node==None:
                return
            left=traverse(node.left)
            right=traverse(node.right)

            node.left,node.right=right,left

            return node
        
        root = traverse(root)
        return root
        
# https://leetcode.com/problems/invert-binary-tree/description/