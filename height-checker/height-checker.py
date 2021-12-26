class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        diff = 0

        for x in range (len(heights)):
            if (target[x]!=heights[x]):
                diff=diff+1

        return(diff)
        