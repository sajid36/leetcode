# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        l = defaultdict(list)
        def multilevel(nestedList, level):
            
            for item in nestedList:
                if item.isInteger():
                    #print("d")
                    l[level].append(item.getInteger())
                    
                else:
                    multilevel(item.getList(), level+1)
        multilevel(nestedList, 1)
        if len(l) == 0 :
            return 0
        maxDepth = max([k for k, v in l.items()])
        res = 0
        for depth, val in l.items():
            for i in val:
                res = res + (maxDepth - depth + 1)* i    
                
        return (res)
            
            
            
            
            
            