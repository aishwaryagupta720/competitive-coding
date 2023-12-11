# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            if temp.val==val:
                if prev!=None:
                    prev.next=temp.next
                else:
                    head=temp.next
                next=temp.next
                temp.next=None
                temp=next
                continue
            prev=temp
            temp=temp.next
        return head
                

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []