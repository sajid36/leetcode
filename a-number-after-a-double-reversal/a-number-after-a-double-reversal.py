class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = str(num)

        temp = str(int(temp[::-1]))
        temp = int(temp[::-1])
        
        return num==temp
        