"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        l = []
        def dfs(node):
            if not node:
                return
            l.append(node)
            dfs(node.left)
            dfs(node.right)
        
        if not root:
            return None
        dfs(root)
        length = len(l) - 1
        if length == 0:
            root.left = root
            root.right = root
            return root
            
        l.sort(key=lambda x:x.val)
        
        
        for pos, node in enumerate (l):
            if pos==0:
                node.left = l[length]
                node.right = l[pos+1]
            elif pos==length:
                node.left = l[pos-1]
                node.right = l[0]    
                
            else:
                node.left = l[pos - 1]
                node.right = l[pos+1]
        
        
        return l[0]