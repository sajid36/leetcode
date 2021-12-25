# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapper = collections.defaultdict(list)
        queue = [(root,0)]
        
        for node, col in queue:
            if node:
                mapper[col].append(node.val)
                queue += [(node.left,col-1),(node.right,col+1)] 
                
        
        res = []
        for index, pair in sorted(mapper.items()):
            res.append(pair)
            
            
            
        return res