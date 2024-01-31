from  typing import *

def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    def toposort(node):
        visited[node] = 1

        for v, w in adjLS[node]:
            if not visited[v]:
                toposort(v)
        st.append(node)
    
    # Step1: Creating a graph
    adjLS = [[]for _ in range(n)]

    for u, v, w in edges:
        adjLS[u].append((v, w))

    # Step2: Find Toposort
    visited = [0] * n
    st = []
    for i in range(n):
        if not visited[i]:
            toposort(i)

    # Step3: Finding Weights
    weights = [float("inf")] * n
    weights[0] = 0

    while st:
        P_node = st.pop()

        for c_node, c_w in adjLS[P_node]:
            if c_w + weights[P_node] < weights[c_node]:
               weights[c_node] = c_w + weights[P_node]
        
    for i in range(n):
        if weights[i] == float("inf"):
            weights[i] = -1
    return weights
