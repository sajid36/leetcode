# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.left = None
        self.right = None
        
        def dfsOne(node):
            if not node:
                return None
            if node==p:
                self.left = node
            if node==q:
                self.right = node
            dfsOne(node.left)
            dfsOne(node.right)

        
        def dfsTwo(node):
            if not node:
                return None
            if node==p or node==q:
                return node
            
            left = dfsTwo(node.left)
            right = dfsTwo(node.right)
            
            if left and right:
                return node
            
            return left if left else right
        
        dfsOne(root)
        if not self.left or not self.right:
            return None
        return dfsTwo(root)
        