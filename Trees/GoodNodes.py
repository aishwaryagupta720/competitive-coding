# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count=0
        def traverse(node,maxm):
            nonlocal count
            if not node:
                return
            if node.val>=maxm:
                count+=1
            maxm=max(maxm,node.val)
            traverse(node.left,maxm)
            traverse(node.right,maxm)
        traverse(root,float("-inf"))
        return count

# if I take maxm as a local variable the maximum value remains local to that node , and when we go back to previous , the maxm of previous is retained

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.