class Solution:
    def dfs(self,node,adj,vis):
        vis[node] = 1
        for it in adj[node]:
            if vis[it] == 0 :
                self.dfs(it,adj,vis)
            
    def findCircleNum(self, adj: List[List[int]]) -> int:
        v = len(adj)
        adjLs = [[] for _ in range(v)]

        for i in range(v):
            for j in range(v):
                if i != j and adj[i][j] == 1:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        
        vis = [0]*v
        cnt = 0

        for i in range(v):
            if vis[i] == 0:
                cnt += 1 
                self.dfs(i,adjLs, vis)
        return cnt