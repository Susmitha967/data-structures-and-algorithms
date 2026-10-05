class Solution:
    def dfs(self,row,col,vis,grid,delrow,delcol):
        n = len(grid);m = len(grid[0])
        vis[row][col] = 1
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            if (0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 'O'):
                self.dfs(nrow,ncol,vis,grid,delrow,delcol)
        
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        vis = [[0]*m for _ in range(n)]
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        for i in range(n):
            if vis[i][0] == 0 and board[i][0] == 'O':
                self.dfs(i,0,vis,board,delrow,delcol)
            if vis[i][m-1] == 0 and board[i][m-1] == 'O':
                self.dfs(i,m-1,vis,board,delrow,delcol)
        for j in range(m):
            if vis[0][j] == 0 and board[0][j] == 'O':
                self.dfs(0,j,vis,board,delrow,delcol)
            if vis[n-1][j] == 0 and board[n-1][j] == 'O':
                self.dfs(n-1,j,vis,board,delrow,delcol)
        

        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        return board