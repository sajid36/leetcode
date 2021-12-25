class Solution:   
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        if x == 2: return 1
        if x == 3: return 1
        
        start = 2
        end = x
        while(True):
            mid = int ((start + end)/2)
            if(mid**2 == x):
                return mid
            elif(mid**2 < x and (mid+1)**2 > x):
                return mid
                
            if(mid**2>x):
                start = start
                end = mid
            else:
                start = mid
                end = end
                
        