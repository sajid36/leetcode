"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        
        seen = {}
        def dfs(node,seen):
            cur = Node(node.val)
            seen[node.val] = cur
            
            nbs = []
            
            for item in node.neighbors:
                if item.val not in seen:
                    nbs.append(dfs(item,seen))
                    
                else:
                    nbs.append(seen[item.val])
                    
            cur.neighbors = nbs
            return cur
        
        
        return dfs(node,seen)
                
                
        