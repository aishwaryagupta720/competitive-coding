# take and fast and a slow pointer , move the fast one twice and slow once at every step , if fast is null in one move , dont move slow
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast:
            fast=fast.next
            if fast:
                fast=fast.next
                slow=slow.next
        return slow
    
    