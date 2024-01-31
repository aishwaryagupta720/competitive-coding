# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        def construct(low,high):
            if low>high:
                return
            mid=(low+high)//2
            root=TreeNode(nums[mid])
            root.left=construct(low,mid-1)
            root.right=construct(mid+1,high)
            return root
        return construct(0,len(nums)-1)
            
            


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced binary search tree.