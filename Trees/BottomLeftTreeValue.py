# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        nodes=[[0,-1]]
        def traverse(node,depth):
            if node==None:
                return 
            if not node.left and not node.right:
                if nodes[0][1]<depth:
                    nodes.pop()
                    nodes.append([node.val,depth])
            traverse(node.left,depth+1)
            traverse(node.right,depth+1)
        traverse(root,0)
        return nodes[0][0]


# Given the root of a binary tree, return the leftmost value in the last row of the tree.
    # https://leetcode.com/problems/find-bottom-left-tree-value/description/