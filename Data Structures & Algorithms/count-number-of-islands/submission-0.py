class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        def dfs(grid,i,j):
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0" 

            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)



        
        count  = 0
        row,cols = len(grid),len(grid[0])

        for i in range(row):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(grid,i,j)
                    count += 1
        
        return count
        
        