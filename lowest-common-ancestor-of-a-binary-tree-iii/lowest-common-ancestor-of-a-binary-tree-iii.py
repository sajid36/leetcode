"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        self.root = None
        res = [p]
        while res:
            cur = res.pop()
            if cur.parent:
                res.append(cur.parent)
            else:
                self.root = cur
                
                
                
        def dfs(node):
            if not node:
                return
            
            if node == p or node==q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            if left and right:
                return node
            
            
            return left if left else right
        
        
        
        return dfs(self.root)