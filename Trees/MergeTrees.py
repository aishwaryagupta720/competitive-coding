# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top Down
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        value=0
        if root1 and root2:
            value=root1.val+root2.val
        elif root1:
            return TreeNode(root1.val)
        elif root2:
            return TreeNode(root2.val)
        else:
            return None
        return self.traverse(root1,root2,TreeNode(value))
    
    def traverse(self,node1,node2,ans):
        print(node1.val,node2.val)
        if node1.left and node2.left:
            ans.left=TreeNode(node1.left.val+node2.left.val)
            self.traverse(node1.left,node2.left,ans.left)
        elif node1.left:
            ans.left=TreeNode(node1.left.val)
            self.traverse(node1.left,TreeNode(),ans.left)
        elif node2.left:
            ans.left=TreeNode(node2.left.val)
            self.traverse(TreeNode(),node2.left,ans.left)

        
        if node1.right and node2.right:
            ans.right=TreeNode(node1.right.val+node2.right.val)
            self.traverse(node1.right,node2.right,ans.right)
        elif node1.right:
            ans.right=TreeNode(node1.right.val)
            self.traverse(node1.right,TreeNode(),ans.right)
        elif node2.right:
            ans.right=TreeNode(node2.right.val)
            self.traverse(TreeNode(),node2.right,ans.right)

        return ans
        

# Bottom Up
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        node = TreeNode()
        left,right=None,None
        if root1 and root2:
            node.val=root1.val+root2.val
            node.left = self.mergeTrees(root1.left,root2.left)
            node.right = self.mergeTrees(root1.right,root2.right)
        elif root1:
            node.val=root1.val
            node.left = self.mergeTrees(root1.left,None)
            node.right = self.mergeTrees(root1.right,None)
        elif root2:
            node.val=root2.val
            node.left = self.mergeTrees(None,root2.left)
            node.right = self.mergeTrees(None,root2.right)
        else:
            return None
        return node
        



        



        





        