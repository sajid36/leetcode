# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, parent):
            if not node:
                return 
            
            if not node.left and not node.right:
                l.append(node.val)
                
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
 

            dfs(node.left, node)
            dfs(node.right, node)
        
        res = list()
        while root.left or root.right:
            l = list()
            dfs(root, root)
            res.append(l)
            
        res.append([root.val])
        return res