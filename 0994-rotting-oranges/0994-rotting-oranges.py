class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid);m = len(grid[0])
        vis = [[0]*m for i in range(n)]

        q = deque()
        tm = 0
        cntFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    vis[i][j] = 2
                    q.append((i,j,0))
                else:
                    vis[i][j] = 0
                
                if grid[i][j] == 1:
                    cntFresh += 1
        
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        cnt = 0;tm = 0
        while q:
            r,c,t = q.popleft()

            tm = max(t,tm)

            for i in range(4):
                nrow = r + delrow[i]
                ncol = c + delcol[i]

                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    q.append((nrow,ncol,t+1))
                    vis[nrow][ncol] = 2
                    cnt +=1
                    
        if cnt == cntFresh:
            return tm
        return -1
                 
        
        