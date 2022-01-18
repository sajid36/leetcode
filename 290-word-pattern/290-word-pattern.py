class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    
        s_list = s.split(" ")
        l = dict()
        if len(pattern) != len(s_list): return False
        if len(set(pattern)) != len(set(s_list)): return False
        
        
        for idx, value in enumerate (s_list):
            if value not in l:
                l[value] = pattern[idx]
            elif l[value]!= pattern[idx]:
                return False
                
                
                
        return True
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

                
        