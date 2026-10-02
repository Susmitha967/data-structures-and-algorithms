class Solution:
    def bfs(self,row,col,adj,vis):
        n = len(adj);m = len(adj[0])
        vis[row][col] = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        q.append((row,col))

        while q:
            row,col = q.popleft()

            for delrow,delcol in directions:
                    nrow = row + delrow
                    ncol = col + delcol

                    if 0 <= nrow < n and 0 <= ncol < m:
                        if adj[nrow][ncol] == '1' and vis[nrow][ncol] == 0:
                            vis[nrow][ncol] = 1
                            q.append((nrow,ncol))
            

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for i in range(n)]
        cnt = 0

        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and grid[i][j] == '1':
                    cnt += 1
                    self.bfs(i,j,grid,vis)
        return cnt
        