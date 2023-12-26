# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            # if both pointers meet at some point
            if fast==slow:
                return True
        return False
        
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
    
# If a cycle exists then the fast and the slow pointers will eventually end ont he same node 