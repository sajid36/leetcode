class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        out = 0
        for x in range (len(J)):
            for y in range (len(S)):
                if(S[y]==J[x]):
                    out = out + 1

        return (out)