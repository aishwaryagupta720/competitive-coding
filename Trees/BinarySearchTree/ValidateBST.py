# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        valueset=sorted(set(values))
        if values!=valueset:
            return False
        else:
            return True



            
# 2nd Approach
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous=[]
        isValid=True
        def validate(node):
            nonlocal isValid
            if not node:
                return
            if len(previous)>=0:
                for i in previous:
                    if i[1]=="left":
                        if i[0]<=node.val:
                            isValid=False
                    elif i[1]=="right":
                        if i[0]>=node.val:
                            isValid=False
            previous.append([node.val,"left"])
            validate(node.left)
            previous.pop()
            previous.append([node.val,"right"])
            validate(node.right)
            previous.pop()

        validate(root)
        return isValid



            