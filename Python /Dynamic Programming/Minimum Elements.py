arr = [1, 2, 3]
t = 8
dp = [[-1] * (t + 1) for _ in range(len(arr))]

def minimum_coins_Recurrsion(arr, t, i):
    if i == 0:
        if t % arr[i] == 0:
            return t // arr[i] 
        return 1e8

    not_take = 0 + minimum_coins_Recurrsion(arr, t, i - 1)
    take = 1e8
    if arr[i] <= t:
        take = 1 + minimum_coins_Recurrsion(arr, t - arr[i], i)

    return min(take, not_take)

# T(C) -> O(2^n)
# S(C) -> O(target)

print(minimum_coins_Recurrsion(arr, t, len(arr)-1))   


def minimum_coins_dp(arr, t, i, dp):

    if i == 0:
        if t % arr[i] == 0:
            return t // arr[i] 
        return 1e8

    if dp[i][t] != -1:
        return dp[i][t]

    not_take = 0 + minimum_coins_Recurrsion(arr, t, i - 1)
    take = 1e8
    if arr[i] <= t:
        take = 1 + minimum_coins_Recurrsion(arr, t - arr[i], i)

    dp[i][t] = min(take, not_take)
    return dp[i][t]

# T(C) -> O(n x target)
# S(C) -> O(n x target) + O(T)

print(minimum_coins_dp(arr, t, len(arr)-1, dp))

def minimum_coins_tab(arr, t, i):
    dp = [[0] * (t + 1) for _ in range(len(arr))]
    for i in range(t + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0] 
        else:
            dp[0][i] = int(1e9)

    for i in range(1, len(arr)):
        for j in range(t + 1):
            not_take = 0 + dp[i - 1][j]
            take = int(1e9)
            if arr[i] <= j:
                take = 1 + dp[i][j - arr[i]]

            dp[i][j] = min(take, not_take)

    res = dp[len(arr)-1][t]
    if res >= int(1e9):
        return 1
    return res 

# T(C) -> O(n x target)
# S(C) -> O(n x target)

print(minimum_coins_tab(arr, t, 0))

def minimum_coins_optimization(arr, t):
    prev = [0] * (t+1)
    for i in range(t + 1):
        if i % arr[0] == 0:
            prev[i] = i // arr[0] 
        else:
            prev[i] = int(1e9)

    for i in range(1, len(arr)):
        curr = [0] * (t + 1)
        for j in range(t + 1):
            not_take = 0 + prev[j]
            take = 1e8
            if arr[i] <= j:
                take = 1 + curr[j - arr[i]]

            curr[j] = min(take, not_take)
        prev = curr[:]

    res = prev[t]
    if res >= int(1e9):
        return -1
    return res

# T(C) -> O(n x target)
# S(C) -> O(target)

print(minimum_coins_optimization(arr, t))

