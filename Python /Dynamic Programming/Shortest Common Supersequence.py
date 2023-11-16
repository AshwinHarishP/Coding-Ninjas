s1 = "brute"  #n = len(s1)
s2 = "groot"  #m = len(s2)

def supersequence_Tab(i, j, s1, s2):
    dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    ans = ""

    for i in range(len(s1) + 1): dp[i][0] = 0
    
    for j in range(len(s2) + 1): dp[0][j] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            
            if s1[i - 1] == s2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = len(s1), len(s2)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans = s1[i - 1] + ans
            i -= 1
            j -= 1
        
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                ans = s1[i - 1] + ans
                i -= 1

            else:
                ans = s2[j - 1] + ans
                j -= 1

    while i > 0:
        ans = ans + s1[i - 1]
        i -= 1
    while j > 0:
        ans = ans + s2[j - 1]
        j -= 1

    return ans

# T(C) -> O(n * m)
# S(C) -> O(n * m)

print(supersequence_Tab(0, 0, s1, s2))

    

    


