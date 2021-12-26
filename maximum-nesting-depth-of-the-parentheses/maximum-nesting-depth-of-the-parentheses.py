class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        current = 0
        for x in range (len(s)):
            if(s[x]=='('):
                current = current + 1
                if(current > maxi):
                    maxi = current
            if(s[x]==')'):
                current = current - 1
                
        return (maxi)
        