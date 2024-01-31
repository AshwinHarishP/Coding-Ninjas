from typing import List
from collections import deque
def toposort(V, adjLs):
    Q = deque()
    Inorder = [0] * V
    res = []

    for i in range(V):
        for j in adjLs[i]:
            Inorder[j] += 1
        
    for i in range(V):
        if Inorder[i] == 0:
            Q.append(i)

    while Q:
        node = Q.popleft()
        res.append(node)

        for i in adjLs[node]:
            Inorder[i] -= 1

            if Inorder[i] == 0:
                Q.append(i)
    return res

def getAlienLanguage(dictionary: List[str], k: int) -> str:

    adjLs = [[]for _ in range(k)]
    for i in range(len(dictionary)-1):
        s1 = dictionary[i]
        s2 = dictionary[i+1]

        length = min(len(s1), len(s2))

        for j in range(length):
            if s1[j] != s2[j]:
                adjLs[ord(s1[j])-97].append(ord(s2[j])-97)
                break
        
        topo = toposort(k, adjLs)
        ans = ""
        for i in topo:
            ans += chr(i + 97)
        return ans
