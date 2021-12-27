# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        l = defaultdict(list)
        
        def dfs(node,level):
            if not node:
                return 
            
            l[level].append(node.val)
            level = level + 1
            dfs(node.left,level)
            dfs(node.right,level)
            
            
        dfs(root,0)
        
        result = []
        i = 1
        for key,val in l.items():
            if i%2==0:
                val.reverse()
                result.append(val)
            else:
                result.append(val)
            i+=1
            
        return (result)
            