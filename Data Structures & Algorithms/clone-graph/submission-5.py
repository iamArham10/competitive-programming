"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

            if node is None:
                return None
            clone_map = {}

            def dfs_clone(node):
                    
                if clone_map.get(node, None):
                    return clone_map[node]
                
                clone = Node(node.val)
                clone_map[node] = clone
                for neighbor in node.neighbors:
                    cloneNeighbor = dfs_clone(neighbor)
                    clone.neighbors.append(cloneNeighbor)

                return clone

            return dfs_clone(node)

                    

        