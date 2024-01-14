# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes=[]
        sum=0
        def generateNumber(x):
            number=0
            for i in range(len(x)):
                number+=x[i]*pow(10,i)
            return number
        def traverse(node):
            nonlocal sum
            if not node:
                return False
            nodes.append(node.val)
            left = traverse(node.left)
            right = traverse(node.right)
            if not left and not right:
                sum=sum+generateNumber(nodes[::-1])
            nodes.pop()
            return True
        
        traverse(root)
        return sum

# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
    
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.