class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col = len(grid),len(grid[0])

        q = deque()
        visit = set()

        def addCell(r,c):
            if(r < 0 or r >= row or c < 0 or c >= col or (r,c) in visit or grid[r][c] == - 1):
                return
            visit.add((r,c))
            q.append([r,c])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


        


        