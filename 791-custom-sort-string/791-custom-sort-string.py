class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = defaultdict()
        
        for item in order:
            if item not in d:
                d[item] = item
                
                
        temp = ""
        for item in s:
            if item in d:
                d[item] = d[item] + item
            else:
                temp = temp + item
                
                
        res=""
        for k,v in d.items():
            res = res + v[1:]
            
            
        return res+temp
                
        