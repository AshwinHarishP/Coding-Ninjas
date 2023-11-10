m = 3
n = 3
dp = [[-1]*n for _ in range(m)]
grid = [[0, 0, 0],[0, -1, 0],[0, 0, 0]]

#Using Recurrsion
def Recurrsion_ways(m, n, grid):
    if m >= 0 and n >= 0 and grid[m][n] == -1:
        return 0

    if m == 0 or n == 0:
        return 1


    return Recurrsion_ways(m - 1, n, grid) + Recurrsion_ways(m, n - 1, grid)



#Using DP
def dp_ways(m, n, grid, dp):
    if m == 0 and n == 0:
        dp[m][n] = 1

    if m < 0 or n < 0 or grid[m][n] == -1:
        return 0
        

    if dp[m][n] != -1:
        return dp[m][n]

    

    dp[m][n] = dp_ways(m - 1, n, grid, dp) + dp_ways(m, n - 1, grid, dp)
    return dp[m][n]



# Using Tabulation
def tabulation_ways(m, n, grid, dp):
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == -1:
                dp[i][j] = 0
            
            if i == 0 and j == 0 and grid[i][j] != -1:
                dp[i][j] = 1
            
            else:

                up = 0
                left = 0
                if i > 0: up = dp[i-1][j]
                if j > 0: left = dp[i][j - 1]

                dp[i][j] = up + left

    return dp[m - 1][n - 1]




# Space Optimization
def Space_optimizaion_way(m, n, grid):

    prev = [-1] * n
    for i in range(m):
        curr = [-1] * n
        for j in range(n):
            
            if grid[i][j] == -1: curr[j] = 0
            
            elif i == 0 and j == 0: curr[j] = 1
        
            else:

                up, left = 0, 0
                if i > 0: up = prev[j]
                if j > 0: left = curr[j-1]

                curr[j] = up + left
        prev = curr

    return prev[n-1]

print(Space_optimizaion_way(m, n, grid))
            
