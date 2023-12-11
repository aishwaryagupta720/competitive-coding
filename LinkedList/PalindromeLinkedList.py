# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True
        fast=head
        slow=head
        # find middle point using fast and slow pointer
        while fast:
            fast=fast.next
            if fast:
                fast=fast.next
            if fast:
                slow=slow.next
        slow=slow.next
        next=slow.next
        slow.next=None
        # reverse the linked list after the middle point to compare 
        while next:
            prev=slow
            slow=next
            next=slow.next
            slow.next=prev
        # compare the halfed linked lists ignore the middle element(odd)
        while slow:
            if slow.val!=head.val:
                return False
            slow=slow.next
            head=head.next
        return True

# Input: head = [1,2,2,1]
# Output: true

