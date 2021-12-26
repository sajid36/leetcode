class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            if(i%2!=0):
                newCharAscii = ord(s[i-1]) + int(s[i])
                result = result + chr(newCharAscii)
            else:
                result = result + s[i]

        return(result)
        