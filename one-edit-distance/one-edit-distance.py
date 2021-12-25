class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)==0 and len(t)==0: return False
        if s==t: return False
        if abs(len(s)-len(t)) > 1: return False
        if len(s)==1 and len(t)==0: return True
        if len(s)==0 and len(t)==1: return True

        counter = 0
        if len(s) == len(t):
            for i in range(len(s)):
                if counter > 1:
                    return False
                if s[i]!=t[i]:
                    counter = counter + 1
            if counter > 1: 
                return False
            else:
                return True

        else:
            if len(s) > len(t):
                big = s
                small = t
            else:
                big = t
                small = s

            for i in range(len(big)):
                #print(small[i],big[i])
                if counter > 1:
                    return False
                if i >= len(small):
                    small = small + '#'
                    
                #print(small)
                if small[i]!=big[i]:
                    counter = counter + 1
                    small = small[0:i] + '#' + small[i:]
            if counter > 1: 
                return False
            else:
                return True