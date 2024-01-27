# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency={}
        def traverse(node):
            if not node :
                return
            frequency[node.val]=frequency.get(node.val,0)+1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        max=0
        keys=[]
        for key,value in frequency.items():
            if max<value:
                max=value
                keys=[key]
            elif max==value:
                keys.append(key)
        return keys

# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
