# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=[[root]]
        ans=[[root.val]]
        for nodes in queue:
            level=[]
            levelval=[]
            for node in nodes:
                if node.left:
                    level.append(node.left)
                    levelval.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    levelval.append(node.right.val)
            if len(level)>0:
                queue.append(level)
                ans.append(levelval)
        return ans            



# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Input: root = [1,2,3,4,null,null,5]
# Output: [[3],[9,20],[15,7]]