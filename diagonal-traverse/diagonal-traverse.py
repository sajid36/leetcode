class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
                    
        res = []   
        for key, val in d.items():
            if key%2==0:
                val.reverse()
            for item in val:
                res.append(item)
                
                
                
        return (res)
        