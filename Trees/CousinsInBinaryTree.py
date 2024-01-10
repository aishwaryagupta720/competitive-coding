# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentxy=None
        def depth(node,parent,cousin):
            nonlocal parentxy
            if node==None:
                return -10
            if node.val==cousin:
                parentxy=parent
                return 0
            left=depth(node.left,node,cousin)+1
            right=depth(node.right,node,cousin)+1

            return max(left,right)

        depthx=depth(root,None,x)
        parentx=parentxy
        depthy=depth(root,None,y)
        parenty=parentxy
        print(depthx,depthy)
        if depthx==depthy and parentx!=parenty:
            return True
        else:
            return False


# cousins are nodes of the tree at the same depth but with different parents
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# https://leetcode.com/problems/cousins-in-binary-tree/description/