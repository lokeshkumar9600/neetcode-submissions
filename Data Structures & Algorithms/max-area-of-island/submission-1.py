class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxarea = 0
        row,col = len(grid),len(grid[0])

        def dfs(grid,i,j):
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0):
                return 0
            
  
            grid[i][j] = 0
            return 1 + dfs(grid,i+1,j) + dfs(grid,i-1,j) + dfs(grid,i,j+1) + dfs(grid,i,j-1)
            

        for i in range(row):
            for j in range(col):
                if(grid[i][j] == 1):
                    area = dfs(grid,i,j)
                    maxarea = max(area,maxarea)
        

        return maxarea

        