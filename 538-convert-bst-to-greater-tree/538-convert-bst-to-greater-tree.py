# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = []
        
        def dfs(node):
            if not node:
                return
            
            l.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
            
        dfs(root)
        
        total = sum(l)
        
        prev = 0
        result = {}
        for item in sorted(l):
            result[item] = total - prev
            prev = prev + item

        
        def dfsReplace(node):
            if not node:
                return
            
            node.val = result[node.val]
            dfsReplace(node.left)
            dfsReplace(node.right)
            
        dfsReplace(root)
        
        return root

            
            
        