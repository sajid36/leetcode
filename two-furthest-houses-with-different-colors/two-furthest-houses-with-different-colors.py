class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maximum = 0
        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                if(colors[i]!=colors[j]):
                    if j-i > maximum:
                        maximum = j - i


        return (maximum)
        