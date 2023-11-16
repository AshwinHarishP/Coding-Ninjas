s1 = "aaa"
s2 = "aa"

def Lcs(s1, s2):
    prev = [0] * (len(s2) + 1)
        
    for i in range(1, len(s1) + 1):
        curr = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]

            else:
                curr[j] = max(prev[j], curr[j - 1])
            
        prev = curr[:]

    res = prev[len(s2)]
    return res

k = Lcs(s1, s2)
n = len(s1)
m = len(s2)

print((n - k) + (m - k))
