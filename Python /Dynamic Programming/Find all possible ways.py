m = 3
n = 3
dp = [[-1] * n for _ in range(m)]

#Using Recussion
def Recussion_ways(m, n):
    if m == 0 and n == 0:
        return 1

    if m < 0 or n < 0:
        return 0

    up = Recussion_ways(m - 1, n) 
    left = Recussion_ways(m, n - 1)

    return up + left


# Using DP
def ways_by_dp(m, n, dp):
    if dp[m][n] != -1:
        return dp[m][n]

    if m == 0 and n == 0:
        return 1

    if m < 0 or n < 0:
        return 0
    

    up = ways_by_dp(m - 1, n, dp)
    left = ways_by_dp(m, n - 1, dp)

    dp[m][n] = up + left

    return dp[m][n]


# Using Tabulation
def ways_by_tabulation(m, n, dp):

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            
            else:

                up = 0
                left = 0
                if i > 0: up = dp[i-1][j]
                if j > 0: left = dp[i][j - 1]

                dp[i][j] = up + left

    return dp[m - 1][n - 1]


# Space Optimization
def ways_by_optimiztion(m, n):
    prev = [-1] * n
    for i in range(m):
        curr = [-1] * n
        for j in range(n):
            
            if i == 0 and j == 0: curr[j] = 1

            else:
                left = 0
                up = 0
                if i > 0: up = prev[j]

                if j > 0: left = curr[j - 1]

                curr[j] = up + left
        prev = curr

    return prev[n - 1]

print(ways_by_optimiztion(m, n))

