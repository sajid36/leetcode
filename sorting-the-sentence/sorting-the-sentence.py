class Solution:
    def sortSentence(self, s: str) -> str:
        localWord = ""
        wordDict = {}
        for char in s:
            if char.isdigit():
                wordDict[int(char)] = localWord
                localWord = ""
            else:
                localWord = localWord + char

        result = ""
        for i in range (1,len(wordDict)+1):
            result = result + wordDict[i].replace(" ", "")
            if(i == len(wordDict)):
                continue
            else: 
                result = result + " "

        return (result)
        