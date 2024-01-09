# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1=[]
        tree2=[]
        def traverse(root,nodes):
            if root.left:
                traverse(root.left,nodes)
            if root.right:
                traverse(root.right,nodes)
            if root.left==None and root.right==None:
                nodes.append(root.val)
        traverse(root1,tree1)
        traverse(root2,tree2)
        return tree1==tree2


# https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-09