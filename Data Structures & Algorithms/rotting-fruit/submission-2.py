class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        visit = set()
        q = deque()

        def addorange(r,c):
            if(r < 0 or r >= row or c < 0 or c >= col or (r,c) in visit or grid[r][c] != 1):
                return

            grid[r][c] = 2
            q.append([r,c])
            visit.add((r,c))


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
        
        
        minute = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                addorange(r + 1, c)
                addorange(r - 1, c)
                addorange(r, c + 1)
                addorange(r, c - 1)
            
            if q:
                minute += 1
        
        for r in range(row):
             for c in range(col):
                 if grid[r][c] == 1:
                    return -1
        

        return minute 

        