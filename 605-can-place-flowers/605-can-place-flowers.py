class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n > 1: return False
            elif n == 0: return True
            else:
                if flowerbed[0] == 0: return True
                else: return False
                    
            
        
        counter = sum(flowerbed)
        for i in range (len(flowerbed)):
            if i == 0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                        
            elif i == len(flowerbed) - 1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
            
            else:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    
                    
                    
                    
        if sum(flowerbed) - counter >= n:
            return True
        else:
            return False
                    
                
                
                        
                
                
        