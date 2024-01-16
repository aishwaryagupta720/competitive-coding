# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node,subNode):
            if not node and not subNode:
                return True
            elif not node or not subNode:
                return False
            if node.val==subNode.val:
                left = traverse(node.left,subNode.left)
                right = traverse(node.right,subNode.right)
                return left and right
            return False
        return traverse(p,q)
            

# https://leetcode.com/problems/same-tree/description/