# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMiddle(self,head):
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        # Breaking link between the Left Tree and Right Tree so when head is passed to recursive function for left tree, it is contained
        if prev:
            prev.next=None
        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        mid=self.findMiddle(head)
        root = TreeNode(mid.val)
        # head is now only the left linked list as we broke the list using prev
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
