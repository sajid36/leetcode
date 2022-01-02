class Solution:
    def checkString(self, s: str) -> bool:
        pos = -1
        flag = 0
        flag1 = 0
        
        for i in range(len(s)):
            if s[i] == 'b' and flag==0:
                flag = 1
                
            if s[i] == 'a' and flag == 1:
                flag1=1
                return False
            if s[i]=='a':
                flag1=1
            
        return True
                
        