class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = {}
        for i in range(len(t)):
            if t[i] in res.keys():
                if (res[t[i]]!= s[i]):
                    return False
            else:
                if s[i] in res.values():
                    return False
                else:
                    res[t[i]] = s[i]
                
            #print(res)
        return True
        