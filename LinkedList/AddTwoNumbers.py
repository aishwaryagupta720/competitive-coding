# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def summation(self,num1,num2,carry):
        sum=num1+num2+carry
        if sum>9:
            return sum%10,sum//10
        return sum,0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummyHead=ListNode()
        dummy=dummyHead
        while l1 or l2:
            dummy.next=ListNode()
            dummy=dummy.next
            if l1 and not l2:
                dummy.val,carry=self.summation(l1.val,0,carry)
                l1=l1.next
            elif l2 and not l1:
                dummy.val,carry=self.summation(0,l2.val,carry)
                l2=l2.next
            else:
                dummy.val,carry=self.summation(l1.val,l2.val,carry)
                l1=l1.next
                l2=l2.next
        if carry>0:
            dummy.next=ListNode()
            dummy=dummy.next
            dummy.val=carry
        return dummyHead.next
        
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
