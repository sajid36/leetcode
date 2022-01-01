# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    l = []
    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            if not node:
                return []
            
            return dfs(node.left) + [node.val] + dfs(node.right)
        
        self.l = dfs(root)
        

    def next(self) -> int:
        return self.l.pop(0)
        

    def hasNext(self) -> bool:
        if len(self.l)==0:
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()