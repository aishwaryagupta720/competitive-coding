# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       
        def traverse(inorder, preorder):
            if not preorder or not inorder:
                return None
            mid = inorder.index(preorder[0])
            root= TreeNode(preorder[0])
            root.left = traverse(inorder[:mid],preorder[1:mid+1])
            root.right = traverse(inorder[mid+1:],preorder[mid+1:])

            return root
        
        return traverse(inorder,preorder)



# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
        
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
