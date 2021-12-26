class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = []
        res.append(n - 1)
        high = heights[n - 1]
        for i in range (n - 2 , -1, -1):
            if heights[i] > high:
                res.append(i)
                high = heights[i]

        return (res[::-1])
                
            
        