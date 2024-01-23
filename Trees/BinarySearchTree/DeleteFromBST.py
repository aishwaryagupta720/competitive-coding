# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        if key<node.val:
            node.left = self.deleteNode(node.left,key)
        elif key>node.val:
            node.right = self.deleteNode(node.right,key)
        else:
            # if the current node is the node to be deleted
            if not node.left:
            # if the left subtree is empty then we will replace current with right subtree
                return node.right
            elif not node.right:
            # if the right subtree is empty then we will replace current with left subtree
                return node.left
            # If both the subtrees exist , then we will replace the key node with the smallest element in the right subtree, to keep the BST valid
            else:
                current=node.right
                prev=node
                while current.left:
                    prev=current
                    current=current.left
                node.val=current.val
                # After we do that we have to delete that smallest element from the right subtree as its a duplicate so we call deleteNode again on it
                #  NOTE here is that initially we move right from the key element then left , so if prev is still the key element , we populate the right subtree, if it has moved then we populate the left subtree
                if prev==node:
                    prev.right = self.deleteNode(current,current.val)
                else: 
                    prev.left = self.deleteNode(current,current.val)
        return node
                

            
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
    
            
                
# https://leetcode.com/problems/delete-node-in-a-bst/