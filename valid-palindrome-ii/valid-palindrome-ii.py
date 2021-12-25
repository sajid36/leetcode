class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left]!=s[right]:
                temp = s[left+1:right+1]
                temp2 = s[left:right]
                if temp==temp[::-1] or temp2==temp2[::-1]:
                    return True
                else:
                    return False
            left = left + 1
            right = right -1   
            
        return True
        