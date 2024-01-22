# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traverse(node):
            if node.val>val:
                if node.left:
                    traverse(node.left)
                else:
                    node.left=TreeNode(val)
                    return
            elif node.val<val:
                if node.right:
                    traverse(node.right)
                else:
                    node.right=TreeNode(val)
                    return
        
        traverse(root)
        return root

# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.