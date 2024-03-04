"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited={}
        def dfs(clone,ognode):
            visited[clone.val]=clone
            for nbr in ognode.neighbors:
                if nbr.val not in visited:
                    cloneneighbor=Node(nbr.val)
                    clone.neighbors.append(cloneneighbor)
                    dfs(cloneneighbor,nbr)
                else:
                    clone.neighbors.append(visited[nbr.val])

        clonegraph=Node(node.val)
        dfs(clonegraph,node)
        return (clonegraph)


        

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }