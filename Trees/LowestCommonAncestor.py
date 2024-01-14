# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This solution find ancestors in a single recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentsp=[]
        parentsq=[]
        foundp=False
        foundq=False
        def traverse(node):
            nonlocal foundp,foundq
            if not node:
                return
            if foundp==True and foundq==True:
                return
            if foundp==False:
                parentsp.append(node)
            if foundq==False:
                parentsq.append(node)
            if node==p:
                foundp=True
            if node==q:
                foundq=True
            traverse(node.left)
            traverse(node.right)
            if foundp==False:
                parentsp.pop()
            if foundq==False:
                parentsq.pop()
        traverse(root)
        # print("P:",parentsp,"Q:",parentsq)
        
        prev=None
        for i,j in zip(range(len(parentsp)),range(len(parentsq))):
            if parentsp[i]!=parentsq[j]:
                print(prev)
                return prev
            prev=parentsp[i]
        return prev



# This solution uses generic recursion function to find ancestors of one node at a time . 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents=[]
        found=False
        def traverse(node,r):
            nonlocal found
            if not node:
                return
            if found==True:
                return
            parents.append(node)
            if node==r:
                found=True
                return
            traverse(node.left,r)
            traverse(node.right,r)
            if found==False:
                parents.pop()
        traverse(root,p)
        parentsp=parents
        parents=[]
        found=False
        traverse(root,q)
        parentsq=parents
        prev=None
        for i,j in zip(range(len(parentsp)),range(len(parentsq))):
            if parentsp[i]!=parentsq[j]:
                print(prev)
                return prev
            prev=parentsp[i]
        return prev