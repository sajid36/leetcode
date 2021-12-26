class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        while(True):
            ordered = sorted(set(s))
            res = res+"".join(ordered)
            for i in range(len(ordered)):
                s = s.replace(ordered[i], '', 1)
            if(len(s)==0): break
            ordered = sorted(set(s))
            res = res+"".join(ordered[::-1])
            for i in range(len(ordered)):
                s = s.replace(ordered[i], '', 1)
            if(len(s)==0): break
                
        return res
        