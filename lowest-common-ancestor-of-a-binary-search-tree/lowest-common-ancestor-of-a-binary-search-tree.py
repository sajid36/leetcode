# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node):
            if not node:
                return
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
                
            elif p.val < node.val and q.val < node.val:
                dfs(node.left)
                
            else:
                self.ans = node
                return
                
        if not root.left and not root.right: return root
        dfs(root)
        return self.ans
        