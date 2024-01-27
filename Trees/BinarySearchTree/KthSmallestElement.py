# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder=[]
        def traverse(node):
            if not node:
                return
            if len(inorder)==k:
                return
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return inorder[k-1]
    

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/