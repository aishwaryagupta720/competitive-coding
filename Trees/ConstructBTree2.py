# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            
        def construct(inorder,postorder):
            if not postorder or not inorder:
                return None
            
            root= TreeNode(postorder[-1])
            mid=inorder.index(postorder[-1])
            root.left = construct(inorder[:mid],postorder[:mid])
            root.right = construct(inorder[mid+1:],postorder[mid:len(inorder)-1])
            return root

            
        return construct(inorder,postorder)
    
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.