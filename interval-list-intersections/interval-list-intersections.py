class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0: return []
        m = len(firstList)
        n = len(secondList)
        i = 0
        j = 0
        
        res = []
        def selection (x,y,i,j):
            if x < y:
                return i+1, j
            elif x == y:
                return i+1, j+1
            else:
                return i, j+1
            
            
        
        while i < m and j < n:
            #print("comparing: ",firstList[i], secondList[j])
            
            if secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                a = max(secondList[j][0], firstList[i][0])
                b = min(secondList[j][1], firstList[i][1])
                
                res.append([a,b])
                i, j = selection(firstList[i][1], secondList[j][1], i, j) 
                
            elif firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                a = max(secondList[j][0], firstList[i][0])
                b = min(secondList[j][1], firstList[i][1])
                
                res.append([a,b])
                i, j = selection(firstList[i][1], secondList[j][1], i, j)    
            else:
                i, j = selection(firstList[i][1], secondList[j][1], i, j)
                
            #print(res)
                
        return (res)
                    
                    
                    
        
                
        
        