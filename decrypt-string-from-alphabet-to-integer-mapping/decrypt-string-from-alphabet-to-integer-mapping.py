class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = ""
        result = ""
        i = 0
        while (i<len(s)):
            print("-> ", s[i])
            if (s[i]!="#"):
                if ((i+2)<len(s) and s[i+2]=='#'):
                    temp = s[i]+s[i+1]
                    result = result + (chr(int(temp)+96))
                    i = i + 3
                else:
                    result = result + (chr(int(s[i])+96))
                    i = i + 1
        return result