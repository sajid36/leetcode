class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s + " "
        word = ""
        result = ""
        count = 0
        for i in range(len(s)):
            if(s[i]==" "):
                result = result + word + " "
                word = ""
                count = count + 1
                if(count==k):
                    break
            else:
                word = word + s[i]


        result = result[:-1]
        return(result)
        