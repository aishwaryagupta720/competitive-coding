# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue=[[root]]
        ans=[root.val]
        for nodes in queue:
            level=[]
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if len(level)>0:
                queue.append(level)
                ans.append(level[-1].val)
        return ans
                


# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# https://leetcode.com/problems/binary-tree-right-side-view/description/
    
# Edge case Input- root=[1,2] , Output- [1,2]