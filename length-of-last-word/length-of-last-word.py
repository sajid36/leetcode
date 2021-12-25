class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = []
        out = s.split()
        if(len(out)>0):
            return (len(out[len(out)-1]))
        else: return 0