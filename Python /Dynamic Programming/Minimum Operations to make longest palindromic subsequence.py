s1 = "codingninjas"
s2 = s1[::-1]

def Longest_palindrome_Optimization(s1, s2):

    prev = [0] * (len(s1) + 1)
    
    for i in range(1, len(s1) + 1):
        curr = [0] * (len(s1) + 1)
        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]

            else:
                curr[j] = max(prev[j], curr[j - 1])
        
        prev = curr[:]

    res = len(s1) - prev[len(s2)]
    return res

print(Longest_palindrome_Optimization(s1, s2))
