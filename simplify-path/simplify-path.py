class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        c = ""
        for item in path + '/':
            if item == '/':
                if c == "..":
                    if stack:
                        stack.pop()
                elif c!="" and c!=".":
                    stack.append(c)
                c = ""
            else:
                c += item
            
        
        return "/" + "/".join(stack)
    
    
    
    
    
    
    
    
    # /home/facebook/