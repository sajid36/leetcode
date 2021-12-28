# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        result = []
        
        def dfs(node):
            if not node:
                return 
            
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        origin = sink = TreeNode(result[0])
        for i in range (1, len(result)):
            sink.right = TreeNode(result[i])
            sink.left = None
            sink = sink.right
            
        root.left=None
        root.right = origin.right