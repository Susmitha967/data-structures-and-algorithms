class Solution:
    def findOrder(self, V: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(V)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        topo = [];q = deque()
        indegree = [0]*V

        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1
            
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)
        if len(topo) == V:
            return topo
        return []

        