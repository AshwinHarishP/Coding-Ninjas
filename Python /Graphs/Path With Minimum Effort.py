from typing import List
from queue import PriorityQueue


def minimumTimeTakingPath(heights: List[List[int]]) -> int:
    def isValid(newR, newC):
        if newR >= 0 and newC >= 0 and newR < n and newC < m:
            return True
        return False
    
    n, m = len(heights), len(heights[0])
    dist = [[float("inf") for _ in range(m)]for _ in range(n)]
    pq = PriorityQueue()
    
    dist[0][0] = 0
    pq.put((0, 0, 0))

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while not pq.empty():
        dis, r, c = pq.get()
        if r == n-1 and c == m-1:
            return dis
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]

            if isValid(newR, newC):
                Effort = max(abs(heights[newR][newC] - heights[r][c]), dis)

                if Effort < dist[newR][newC]:
                    dist[newR][newC] = Effort
                    pq.put((Effort, newR, newC))
    return 0
