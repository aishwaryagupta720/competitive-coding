# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    absolute=0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.absolute
    def traverse(self,node):
        if not node:
            return 0
        left = self.traverse(node.left)
        right= self.traverse(node.right)
        self.absolute = self.absolute+abs(left-right)
        return left+right+node.val #sum of subtree

        
        