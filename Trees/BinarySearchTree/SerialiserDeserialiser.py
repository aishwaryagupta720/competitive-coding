'''Using Beadth First Search'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "-1"
        queue=[root]
        serial=str(root.val)
        for node in queue:
            if node.left:
                queue.append(node.left)
                serial+=","
                serial+=str(node.left.val)
            else:
                serial+=","
                serial+="-1"
            
            if node.right:
                queue.append(node.right)
                serial+=","
                serial+=str(node.right.val)
            else:
                serial+=","
                serial+="-1"
        return serial


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes=data.split(",")
        if nodes[0]=="-1":
            return None
        root=TreeNode(int(nodes.pop(0)))
        queue=[root]
        for node in queue:
            if nodes[0]!="-1":
                node.left = TreeNode(int(nodes[0]))
                queue.append(node.left)
            nodes.pop(0)
            if nodes[0]!="-1":
                node.right = TreeNode(int(nodes[0]))
                queue.append(node.right)
            nodes.pop(0)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
    


'''Using Depth First Search'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        preorder=[]
        def dfs(node):
            if not node:
                preorder.append("-1")
                return
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(preorder)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data=="":
            return None
        preorder=data.split(",")
        def dfs():
            if preorder[0]=="-1":
                preorder.pop(0)
                return None
            root=TreeNode(int(preorder.pop(0)))
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans