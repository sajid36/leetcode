class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def dfs(x,y,count):
            grid[x][y] = count            
            if x+1 < m and grid[x+1][y]=="1":
                dfs(x+1,y,count)
                
            if x-1 >= 0 and grid[x-1][y]=="1":
                dfs(x-1,y,count)
                
            if y+1 < n and grid[x][y+1]=="1":
                dfs(x,y+1,count)
                
            if y-1 >= 0 and grid[x][y-1]=="1":
                dfs(x,y-1,count)

            
            
        total = "2"
        for i in range (m):
            for j in range (n):
                if grid[i][j] == "1":
                    dfs(i,j,total)
                    total = str(int(total) + 1)
                    
                    
        
        if int(total)==2: return 0
        elif int(total) - 2 == 1:
            return 1
        else:
            return int(total)-2