class Solution:
    def trap(self, height: List[int]) -> int:
        
        trapped = 0
        maxLeft = []
        maxRight = []
        maxL = 0
        maxR = 0
        n = len(height) - 1
        for i in range (len(height)):
            maxLeft.append(maxL)
            if height[i] > maxL:
                maxL = height[i]
                
            
            maxRight.append(maxR)
            if height[n - i] > maxR:
                maxR = height[n-i]
                
        maxRight = maxRight[::-1]
                
        
        for i in range (1,len(height)-1):
            mini = min (maxLeft[i], maxRight[i]) - height[i]
            if mini > 0:
                trapped = trapped + mini
            
            
            
        return (trapped)
            
        