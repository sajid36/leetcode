class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = str(num)
        if len(temp)==1 and temp=="0": return True

        if temp[-1]=="0":
            return False
        else:
            return True
                
        