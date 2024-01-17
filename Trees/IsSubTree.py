# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def traverse(node):
            if not node:
                return False

            if node.val==subRoot.val :
                subtree = isSameTree(node,subRoot)
            else:
                subtree=False

            left = traverse(node.left)
            right = traverse(node.right)
            
            return (subtree or left or right)
        
        def isSameTree(node,subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val==subnode.val:
                left=isSameTree(node.left,subnode.left)
                right=isSameTree(node.right,subnode.right)
                return left and right
            else: return False
        
        return (traverse(root))
        

# https://leetcode.com/problems/subtree-of-another-tree/
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.         


        
        


