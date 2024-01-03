# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def treeTraversal(root):
            if root==None:
                return
            result.append(root.val)
            left=treeTraversal(root.left)
            if left:
                result.append(left.val)
            right=treeTraversal(root.right)
            if right:
                result.append(right.val)

        treeTraversal(root)
        return result


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]