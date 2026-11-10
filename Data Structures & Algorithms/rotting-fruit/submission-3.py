class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])


        visited = set()
        q = deque()


        def addOrange(i,j):
            if i < 0 or i >= row or j < 0 or j >= cols or (i,j) in visited or grid[i][j] != 1:
                return

            grid[i][j] = 2
            q.append([i,j])
            visited.add((i,j))
        
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visited.add((i,j))
        
        minute = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addOrange(r + 1, c)
                addOrange(r - 1, c)
                addOrange(r, c + 1)
                addOrange(r, c - 1)
            
            if q:
                minute += 1

        

        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minute
        


            



        