class Solution:
    def bfs(self,start,adj,color):
        q = deque()
        q.append(start)
        color[start] = 0
        while q:
            node = q.popleft()

            for it in adj[node]:
                if color[it] == -1:
                    color[it] = 1 - color[node]
                    q.append(it)
                elif color[it] == color[node]:
                    return False
        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:
        
        color = [-1]*len(graph)

        for i in range(len(graph)):
            if color[i] == -1:
                if self.bfs(i,graph,color) == False:
                    return False
        return True