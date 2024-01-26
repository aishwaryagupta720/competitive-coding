# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator=float(-inf)
        self.previous=[None]
        self.inorder=[]
        traverse(root)
        
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        self.inorder.append(node)
        traverse(node.right)

    def next(self) -> int:
        if self.iterator==float(-inf):
            print(self.iterator,"start")
            if not self.root:
                return None
            self.iterator=self.root
            while self.iterator.left:
                self.previous.append(self.iterator)
                self.iterator=self.iterator.left
        else:
            if self.iterator.right:
                print(self.iterator.val,"right")
                self.previous.append(self.iterator)
                self.iterator=self.iterator.right
                while self.iterator.left:
                    self.previous.append(self.iterator)
                    self.iterator=self.iterator.left
            else:
                print(self.iterator.val,"backtrack")
                if self.previous[-1].left==self.iterator:
                    self.iterator=self.previous.pop()
                else:
                    while True:
                        if self.previous[-1].right==self.iterator:
                            self.iterator=self.previous.pop()
                        else:
                            break
                    self.iterator=self.previous.pop()
        return self.iterator.val
    
    def hasNext(self) -> bool:
        if self.iterator==float(-inf) and self.root:
            return True
        elif self.iterator.right:
            return True
        elif self.previous[-1] and self.previous[-1].left==self.iterator:
            return True
        else :
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()