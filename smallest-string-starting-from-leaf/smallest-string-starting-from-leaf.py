# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node,result):
            if not node:
                return 
            result = result + chr(node.val+97)
            if node.left and node.right:
                dfs(node.right,result)
                dfs(node.left,result)
                
            elif node.left and not node.right:
                dfs(node.left,result)
                
                
            elif not node.left and node.right:
                dfs(node.right,result)
                
                    
            elif not node.left and not node.right:
                res.append(result[::-1])
                
        
        
        dfs(root,'')
        res.sort()
        return res[0]