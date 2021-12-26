class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        print(len(mat))
        result = 0
        count = 0
        for i in mat:
            result = result + i[count]
            if(count!=abs(len(mat)-count-1)):
                result = result + i[abs(len(mat)-count-1)]
            count +=1
        return(result)
                