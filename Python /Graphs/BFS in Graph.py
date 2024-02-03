from typing import List
from collections import deque
def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    def bfs(node):
        Q.append(node)
        visited[node] = 1
        while Q:
            p_node = Q.popleft()
            res.append(p_node)

            for i in adj[p_node]:
                if not visited[i]:
                    Q.append(i)
                    visited[i] = 1

    Q = deque()
    visited = [0] * n
    res = []
    bfs(0)
    return res
