class Solution:
    def romanToInt(self, s: str) -> int:
        x = len(s)
        res = 0
        for i in range (x):
            if s[i]=='I':
                if(i==x-1):
                    res = res + 1
                    print("here")
                else:
                    if(s[i+1]=='V' or s[i+1]=='X'):
                        res = res - 1
                    else:
                        res = res + 1
            if s[i]=='V':
                res = res + 5
            if s[i]=='X':
                if(i==x-1):
                    res = res + 10
                else:
                    if(s[i+1]=='L' or s[i+1]=='C'):
                        res = res - 10
                    else:
                        res = res + 10
            if s[i]=='L':
                res = res + 50
            if s[i]=='C':
                if(i==x-1):
                    res = res + 100
                else:
                    if(s[i+1]=='D' or s[i+1]=='M'):
                        res = res - 100
                    else:
                        res = res + 100
            if s[i]=='D':
                res = res + 500
            if s[i]=='M':
                res = res + 1000
        return res