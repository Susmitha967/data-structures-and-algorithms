class Solution:
    def dfs(self,row,col,newC,iCol,image,ans,delRow,delCol):
        ans[row][col] = newC
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]
            if 0 <= nrow < n and 0 <= ncol < m and image[nrow][ncol] == iCol and ans[nrow][ncol] != newC:
                self.dfs(nrow,ncol,newC,iCol,image,ans,delRow,delCol)
        
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        initColor = image[sr][sc]
        ans = [row[:] for row in image]
        delRow = [-1,0,1,0]
        delCol = [0,1,0,-1] 
        self.dfs(sr,sc,newColor,initColor,image,ans,delRow,delCol)  
        return ans     