class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = [None] * len(s)
        for x in range (len(indices)):
            out[indices[x]] = s[x]
            
        out = ''.join(out)
        return out
        #print(out)
        
        