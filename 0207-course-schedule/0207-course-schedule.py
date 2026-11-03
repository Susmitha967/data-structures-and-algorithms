
from collections import deque
from typing import List


class Solution:
    def canFinish(self, V: int, prerequisites: List[List[int]]) -> bool:

        # Form a graph
        adj = [[] for _ in range(V)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        
        topo = []
        indegree = [0]*V

        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1
        
        q = deque()
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
            return True
        return False
