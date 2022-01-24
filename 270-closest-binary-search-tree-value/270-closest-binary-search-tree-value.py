# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        self.mini = float('inf')
        self.res = None
        
        def dfs(node):
            if not node:
                return
            
            if self.mini > abs(target - node.val):
                self.mini = abs(target - node.val)
                self.res = node.val
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.res
        