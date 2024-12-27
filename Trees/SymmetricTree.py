# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compareSides(root.left,root.right)

    def compareSides(self,leftnode,rightnode):
        if not leftnode and not rightnode:
            return True
        elif not leftnode or not rightnode:
            return False
        elif leftnode.val==rightnode.val:
            side1 = self.compareSides(leftnode.right,rightnode.left)
            side2 = self.compareSides(leftnode.left,rightnode.right)
        else:
            return False
        return side1 and side2

        

        

#         101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

