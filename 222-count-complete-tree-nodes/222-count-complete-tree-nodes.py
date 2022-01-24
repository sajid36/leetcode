# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = [0]
        def dfs(node):
            if not node:
                return
            res[0] = res[0] + 1
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        
        
        return res[0]
        
        