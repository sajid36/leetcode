class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        
        for i in range (len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                
            if s[i] == ')':
                if (len(stack)==0): return False
                item = stack.pop()
                if item!='(':
                    return False
            
            if s[i] == '}':
                if (len(stack)==0): return False
                item = stack.pop()
                if item!='{':
                    return False
            
            if s[i] == ']':
                if (len(stack)==0): return False
                item = stack.pop()
                if item!='[':
                    return False
                
        if (len(stack)==0): return True
        else: return False
        