class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)==1: return s
        
        res = [s[0]]
        for i in range(1,len(s)):
            if len(res)==0:
                res.append(s[i])
                continue
                
            if s[i]==res[len(res)-1]:
                res.pop()
            else:
                res.append(s[i])
                   
        return ''.join(res)
            
        