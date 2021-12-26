# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:  
        result = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if (node.val >= low and node.val<= high):
                    result = result + node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        
        return (result)
        
   
        