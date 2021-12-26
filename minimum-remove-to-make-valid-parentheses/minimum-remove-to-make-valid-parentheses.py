class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cur = ''
        for ch in s:
            if ch == '(':
                stack.append(cur)
                #print(stack)
                cur = ''
            elif ch == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')' 
                    #print(cur)
            else:
                cur += ch
       
        #print("cur", cur)
        while stack:
            cur = stack.pop() + cur
        
        return cur
            

                
        
        