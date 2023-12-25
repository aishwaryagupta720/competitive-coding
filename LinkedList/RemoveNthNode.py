# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast=head,head
        count=n
        prev=None
        while count>0:
            fast=fast.next
            count-=1
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        if prev!=None:
            prev.next=slow.next
        elif slow.next!=None:
            head=slow.next
        else:
            head=None
        return head

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]