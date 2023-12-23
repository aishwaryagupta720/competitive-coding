# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle
        slow,fast=head,head
        while fast:
            fast=fast.next
            if fast:
                fast=fast.next
                slow=slow.next
        # reverse second half list
        prev=None        
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        temp=head
        maxm=0
        # sum of values of first and second half lists and find max
        while prev:
            maxm=max(maxm,prev.val+temp.val)
            temp=temp.next
            prev=prev.next
        return maxm


# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 
    
# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
