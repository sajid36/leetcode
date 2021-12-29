# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node,pre):
            if not node:
                return
            
            cur = "->" + str(node.val)
            
            if not node.left and not node.right:
                result.append(pre+cur)
            else:
                dfs(node.left,pre+cur)
                dfs(node.right,pre+cur)
        
        
        if not root.left and not root.right:
            return [str(root.val)]
        
        elif not root.left and root.right:
            dfs(root.right,str(root.val))
          
        elif root.left and not root.right:
            dfs(root.left,str(root.val))
        else:
            dfs(root.left,str(root.val))
            dfs(root.right,str(root.val))

            
        return result
        