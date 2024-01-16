# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Depth First Search
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def traverse(node):
            if not node:
                return 0
            left=traverse(node.left)
            right=traverse(node.right)
            # if left/right tree is empty (0) then we take the non-empty tree
            if left>0 and right>0:
                return min(left,right)+1
            else: return max(left,right)+1
            
        return traverse(root)
        
        
# Breadth First Search
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=[[root]]
        depth=0
        for nodes in queue:
            level=[]
            depth+=1
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if not node.left and not node.right:
                    return depth
            if len(level)>0:
                queue.append(level)

            