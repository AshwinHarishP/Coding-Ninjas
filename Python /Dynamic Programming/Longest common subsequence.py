s1, s2 = "adcbe", "dcadb"
n, m = len(s2), len(s1)
dp = [[-1] * (m + 1) for _ in range(n + 1)]
def subsequence_R(i, j, s1, s2):
    if i == 0 or j == 0:
        return 0
    
    if s1[i - 1] == s2[j - 1]:
        return 1 + subsequence_R(i - 1, j - 1, s1, s2)

    return max(subsequence_R(i - 1, j, s1, s2), subsequence_R(i, j - 1, s1, s2))

# T(C) -> O(Exponential)
# S(C) -> O(n * m)

print(subsequence_R(n, m, s1, s2))

def subsequence_dp(i, j, s1, s2, dp):
    
    if i == 0 or j == 0:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i - 1] == s2[j - 1]:
        dp[i][j] =  1 + subsequence_dp(i - 1, j - 1, s1, s2, dp)
    else:

        dp[i][j] =  max(subsequence_dp(i, j - 1, s1, s2, dp), subsequence_dp(i - 1, j, s1, s2, dp))

    return dp[i][j]

# T(C) -> O(n * m)
# S(C) -> O(n * m) + O(n * m)

print(subsequence_dp(n, m, s1, s2, dp))


def subsequence_Tab(i, j, s1, s2):
    dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        dp[i][0] = 0
    for j in range(len(s2) + 1):
        dp[0][j] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]

# T(C) -> O(n * m)
# S(C) -> O(n * m)

print(subsequence_Tab(0, 0, s1, s2))

def subsequence_optimization(i, j, s1, s2):
    prev = [0]*(len(s1)+1)
    for i in range(len(s1)+1):
        prev[i] = 0
    
    for i in range(1, len(s1) + 1):
        curr = [0]*(len(s1) + 1)
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev = curr[:]
    return prev[len(s2)]

# T(C) -> O(n * m)
# S(C) -> O(m)

print(subsequence_optimization(0, 0, s1, s2))

def subsequence_optimization2(i, j, s1, s2):
    prev = [0]*(len(s1)+1)
    for i in range(len(s1)+1):
        prev[i] = 0
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                prev[j] = 1 + prev[j - 1]
            else:
                prev[j] = max(prev[j], prev[j - 1])

    return prev[len(s2)]

# T(C) -> O(n * m)
# S(C) -> O(m)

print(subsequence_optimization2(0, 0, s1, s2))
