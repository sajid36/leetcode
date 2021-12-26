class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        maximum = 0
        for i in range (len(gain)):
            result = result + gain[i]
            if(result>maximum):
                maximum = result
        return(maximum)
        