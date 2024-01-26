# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator=-1
        self.inorder=[]
        self.traverse(root)
        self.index=-1
        
    def traverse(self,node):
        if not node:
            return
        self.traverse(node.left)
        self.inorder.append(node)
        self.traverse(node.right)

    def next(self) -> int:
        if self.iterator==-1:
            self.iterator=self.inorder[0]
            self.index=0
        else:
            if self.hasNext():
                self.index+=1
                self.iterator=self.inorder[self.index]
        return self.iterator.val


    
    def hasNext(self) -> bool:
        if self.index+1<=len(self.inorder)-1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
        


# Approach 2 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder=TreeNode(-1,None,None)
        self.head=self.inorder
        self.traverse(root)
        self.iterator=self.head
        
    def traverse(self,node):
        if not node:
            return
        self.traverse(node.left)
        self.inorder.right=node
        node.left=None
        self.inorder=self.inorder.right
        self.traverse(node.right)

    def next(self) -> int:
        if self.hasNext():
            self.iterator=self.head.right
            self.head=self.head.right
        return self.iterator.val

    
    def hasNext(self) -> bool:
        if self.head.right:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()