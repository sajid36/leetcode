class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        result = 0
        for i in range (len(s)):
            if (s[i] == 'R'):
                count  = count + 1
            else: count = count - 1
            
            if (count == 0):
                result = result + 1
        return (result)
        