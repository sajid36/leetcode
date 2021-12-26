class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allow = list(allowed)
        count = 0
        for i in words:
            flag = 0
            for j in i:
                if j in allow:
                    continue
                else:
                    flag = 1
            if(flag==1):
                continue
            else:
                count = count + 1
                
        return(count)
        