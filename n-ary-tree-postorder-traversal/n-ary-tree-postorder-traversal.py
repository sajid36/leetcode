"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []
        if not root.children: return [root.val]
        lst = []
        for item in root.children: lst += self.postorder(item)
        return lst + [root.val]
        