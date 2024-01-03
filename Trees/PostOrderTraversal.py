# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def treeTraversal(root):
            if root==None:
                return
            treeTraversal(root.left)

            treeTraversal(root.right)

            result.append(root.val)
        
        treeTraversal(root)
        return result
            
            

            
            
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]