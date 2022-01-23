class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        res = defaultdict(list)
        
        for i in range (n):
            item = []
            for j in range (n):
                item.append(matrix[j][i])
            res[i].append(item[::-1])
        
        
        for i in range (n):
            for j in range (n):
                matrix[i][j] = res[i][0][j]