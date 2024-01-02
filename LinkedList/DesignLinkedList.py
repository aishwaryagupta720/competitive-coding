class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def get(self, index: int) -> int:
        dummy=self.head
        while index>0 and dummy.next:
            dummy=dummy.next
            index-=1
        if index==0 and dummy:
            return dummy.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node=Node(val,None)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node

    def addAtTail(self, val: int) -> None:
        node=Node(val,None)
        if self.tail==None:
            self.tail=node
            self.head=node
        else:
            self.tail.next=node
            self.tail=node
        
    def addAtIndex(self, index: int, val: int) -> None:
        dummy=self.head
        prev=None
        while index>0 and dummy:
            prev=dummy
            dummy=dummy.next
            index-=1
        if index==0 and dummy:
            node=Node(val,dummy)
            if prev:
                prev.next=node 
            else:
                self.addAtHead(val)
        elif index==0 and dummy==None:
            self.addAtTail(val) 

    def deleteAtIndex(self, index: int) -> None:
        dummy=self.head
        prev=None
        while index>0 and dummy:
            prev=dummy
            dummy=dummy.next
            index-=1
        if index==0 and dummy:
            if prev and dummy.next:
                prev.next=dummy.next
            elif self.head==dummy and self.tail!=dummy:
                self.head=dummy.next
            elif self.tail==dummy and self.head!=dummy:
                self.tail=prev
                prev.next=None
            else:
                self.head=None
                self.tail=None

    def printlist(self):
        dummy=self.head
        while dummy:
            print(dummy.val,end="", flush=True)
            print("-->",end="", flush=True)
            dummy=dummy.next
        print("")        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
        
# https://leetcode.com/problems/design-linked-list/description/  
# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
