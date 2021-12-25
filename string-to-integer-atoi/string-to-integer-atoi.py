class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 : return 0
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        
        sign = 1
        i = 0
        if ls[0] =='-':
            sign = -1
            del ls[0]
        elif ls[0] =='+':
            del ls[0]
            
        res = 0
        while i < len(ls) and ls[i].isdigit():
            #print("hre")
            res = res *10 + int(ls[i])
            i += 1
            
        return max(min ((res*sign),2**31 -1), -2**31)