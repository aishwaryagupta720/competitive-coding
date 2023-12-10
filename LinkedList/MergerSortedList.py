# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        temp=ListNode()
        slist=temp
        while curr1 and curr2:
            if curr1.val<curr2.val:
                slist.next=curr1
                curr1=curr1.next
                slist=slist.next
            elif curr1.val==curr2.val:
                slist.next=curr1
                slist=slist.next
                curr1=curr1.next
                slist.next=curr2
                slist=slist.next
                curr2=curr2.next
            else:
                slist.next=curr2
                curr2=curr2.next
                slist=slist.next
        if curr1==None:
            curr1=curr2
        while curr1:
            slist.next=curr1
            curr1=curr1.next
            slist=slist.next 
        return temp.next

        
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
