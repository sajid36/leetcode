# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        result = []
        
        def dfs (node, temp):
            if not node:
                return
            temp = temp + str(node.val)
            #print(temp)
            
            if not node.left and not node.right:
                result.append(int(temp))
            
            dfs(node.left, temp)
            dfs(node.right, temp)
            
            
            
            
            
        dfs(root,'')
        
        return (sum(result))
        