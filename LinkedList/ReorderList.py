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

