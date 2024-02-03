from collections import deque
def cycleDetection(edges, n, m):
    def isCycle(node):
        Q.append((node, -1))
        visited[node] = 1

        while Q:
            node, parent = Q.popleft()
            for i in adjLs[node]:
                if not visited[i]:
                    Q.append((i, node))
                    visited[i] = 1

                elif parent != i:
                    return True
        return False

    Q = deque()
    visited = [0]*(n+1)
    
    adjLs =[[]for _ in range(n+1)]
    for u, v in edges:
        adjLs[u].append(v)
        adjLs[v].append(u)

    for i in range(1, n+1):
        if not visited[i]:
            if isCycle(i):
                return "Yes"
    return "No"
