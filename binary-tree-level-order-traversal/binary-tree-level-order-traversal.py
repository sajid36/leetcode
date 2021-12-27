# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        l = defaultdict(list)
                
        def dfs(node, level):
            if not node:
                return 
            l[level].append(node.val)
            level = level + 1
            dfs(node.left,level)
            dfs(node.right,level)

        dfs(root,0)
        return [value for key, value in sorted(l.items())]
        