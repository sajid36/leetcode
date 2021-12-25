class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        queue = []
        counter = 0
        for ch in s:
            if ch == '(':
                queue.append(ch)
                
                
            else:
                if queue:
                    queue.pop()
                else:
                    counter = counter + 1
                    
                    
                    
        if len(queue):
            
            counter = counter + len(queue)
            
            
        return counter
                    
        