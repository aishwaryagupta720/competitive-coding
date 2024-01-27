# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum=0
        def traverse(node):
            nonlocal sum
            if not node:
                return
            if low<=node.val<=high:
                sum+=node.val
                traverse(node.left)
                traverse(node.right)
            elif node.val<low:
                traverse(node.right)
            elif node.val>high:
                traverse(node.left)
        
        traverse(root)
        return sum
            
# https://leetcode.com/problems/range-sum-of-bst/description/
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].