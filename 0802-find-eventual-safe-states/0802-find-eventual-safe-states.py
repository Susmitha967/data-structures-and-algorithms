class Solution:
    def dfs(self,node,vis,pathVis,adj,check):
        vis[node] = 1
        pathVis[node] = 1
        check[node] = 0
        for i in adj[node]:
            if vis[i] == 0:
                if self.dfs(i,vis,pathVis,adj,check):
                    return True
            elif pathVis[i] == 1:
                return True
        check[node] = 1
        pathVis[node] = 0
        
        return False 
    def eventualSafeNodes(self, edges: list[list[int]]) -> list[int]:
        vis = [0]*len(edges)
        pathVis = [0]*len(edges)
        check = [0]*len(edges)
        for i in range(len(edges)):
            if vis[i] == 0:
                self.dfs(i,vis,pathVis,edges,check)
                    
        
        safeNodes = []
        for i in range(len(edges)):
            if check[i] == 1:
                safeNodes.append(i)
        return safeNodes
        
