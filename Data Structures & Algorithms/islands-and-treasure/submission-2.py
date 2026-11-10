class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        row = len(grid)
        cols = len(grid[0])

        def addCells(i,j):
            if i >= row or i < 0 or j >= cols or j < 0 or (i,j) in visited or grid[i][j] == -1:
                return
            
            visited.add((i,j))
            q.append([i,j])

        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append([i,j])

        dist = 0
        while q:
            for i in range(len(q)):
                r,c  = q.popleft()
                grid[r][c] = dist
                addCells(r + 1, c)
                addCells(r - 1, c)
                addCells(r, c + 1)
                addCells(r, c - 1)
            dist += 1




        