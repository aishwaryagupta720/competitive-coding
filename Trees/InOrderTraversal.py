# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def traverseTree(root):
            if root==None:
                return
            left=traverseTree(root.left)
            if left:
                result.append(left.val)

            result.append(root.val)
            
            right=traverseTree(root.right)
            if right:
                result.append(right.val)
            
        traverseTree(root)
        return result


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]