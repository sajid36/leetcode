class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for item in operations:
            if(item[1]=='+'):
                res = res + 1
            else:
                res = res - 1
        return (res)
        