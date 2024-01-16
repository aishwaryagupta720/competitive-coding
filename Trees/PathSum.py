# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum=0
        found=False
        def traverse(node):
            nonlocal found,sum
            if not node:
                return False
            if found==True:
                return
            sum=sum+node.val
            print(sum)
            left = traverse(node.left)
            right = traverse(node.right)
            if not left and not right:
                if sum==targetSum:
                    found=True
            sum=sum-node.val
            return True

        traverse(root)
        return found

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
    
# https://leetcode.com/problems/path-sum/description/