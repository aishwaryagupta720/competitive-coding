# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node):
            left,right=None,None
            if not node:
                return None
            if node.val==val:
                return node
            elif node.val>val:
                return traverse(node.left)
            else:
                return traverse(node.right)
            

        
        return traverse(root)


# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# https://leetcode.com/problems/search-in-a-binary-search-tree/description/