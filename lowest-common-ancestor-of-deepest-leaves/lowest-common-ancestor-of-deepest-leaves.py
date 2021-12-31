# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        l = defaultdict(list)
        res = []
        
        
        def dfs(node, level):
            if not node:
                return node
            
            l[level].append(node)
            
            level = level + 1
            dfs(node.left,  level)
            dfs(node.right, level)
        
        
        def dfsTwo(node):
            if not node:
                return node
            
            if node in res:
                return node
            
            left = dfsTwo(node.left)
            right = dfsTwo(node.right)
            
            if left and right:
                return node
            
            return left if left else right 
            
        
        
        if not root.left and not root.right: return root
        dfs(root, 0)
        res = l[len(l)-1]
        
        return dfsTwo(root)
        
        
        