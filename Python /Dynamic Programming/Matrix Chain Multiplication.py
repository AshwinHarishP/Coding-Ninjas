arr = [10, 20, 30, 40, 50]
n = len(arr)

def f_Recursion(i, j, arr):
    mini = int(1e9)
    k = i
    if i == j: 
        return 0

    for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + f_Recursion(i, k, arr) + f_Recursion(k + 1, j, arr)

        if (steps < mini):
            mini = steps

    return mini

print(f_Recursion(1, n-1, arr))
# T(C) -> O(2 ^ n) - exponential
# S(C) -> O(n)

def f_memo(i, j, arr, dp):

    mini = int(1e9)
    if i == j: 
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    
    for k in range(i, j):
        steps = arr[i - 1] * arr[k] * arr[j] + f_memo(i, k, arr, dp) + f_memo(k + 1, j, arr, dp)

        if (steps < mini):
            mini = steps
    dp[i][j] = mini

    return dp[i][j]

dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
print(f_memo(1, n-1, arr, dp))

# T(C) -> O(n^3)
# S(C) -> O(n ^ 2) + O(n)

def f_tab(i, j, arr, dp):
    
    for i in range(len(arr)):
        dp[i][i] = 0

    for i in range(len(arr)-1, 0, -1):
        for j in range(i+1, len(arr)):

            mini = int(1e9)
            for k in range(i, j):
                steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]

                if (steps < mini):
                    mini = steps
            dp[i][j] = mini
    return dp[i][j]

dp = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
print(f_tab(1, n-1, arr, dp))

# T(C) -> O(n ^ 3)
# S(C) -> O(n * n)
