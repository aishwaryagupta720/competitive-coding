# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return []
        root = TreeNode(val=preorder[0])
        if len(preorder)==1:
            return root

        def splitter(root,inorder,preorder):
            left=inorder[0:inorder.index(root)]
            right=inorder[inorder.index(root)+1:len(inorder)]
            preright,preleft=[],[]
            if len(left)>0:
                for i in preorder:
                    if i in left:
                        preleft.append(i)
                lefttree = splitter(preleft[0],left,preleft)
            else:
                lefttree = None
            if len(right)>0:
                for i in preorder:
                    if i in right:
                        preright.append(i)
                righttree = splitter(preright[0],right,preright[1:len(preright)])
            else:
                righttree = None
            return TreeNode(root,lefttree,righttree)

        return (splitter(root.val,inorder,preorder[1:len(preorder)]))

        
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
        
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
