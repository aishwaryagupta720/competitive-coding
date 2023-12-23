# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        # get middle
        while fast:
            fast=fast.next
            if fast:
                fast=fast.next
            if fast:
                slow=slow.next
        left=slow
        slow=slow.next
        left.next=None
        # reverse second half
        prev=None
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        temp=head
        slow=prev
        # reorder list
        while slow:
            lnext=temp.next
            rnext=slow.next
            temp.next=slow
            slow.next=lnext
            temp=lnext
            slow=rnext
        return head



# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
