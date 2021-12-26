class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        res1 = ""
        for i in range (len(firstWord)):
            temp = ord(firstWord[i]) - ord('a')
            res1 = res1 + str(temp)

        res2 = ""
        for i in range (len(secondWord)):
            temp = ord(secondWord[i]) - ord('a')
            res2 = res2 + str(temp)

        res3 = ""
        for i in range (len(targetWord)):
            temp = ord(targetWord[i]) - ord('a')
            res3 = res3 + str(temp)

        if(int(res1)+int(res2)==int(res3)):
            return True
        else:
            return False

        