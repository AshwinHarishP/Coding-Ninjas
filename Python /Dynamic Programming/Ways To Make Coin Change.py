arr = [1, 2, 3]
t = 4
dp = [[-1] * (t + 1) for _ in range(len(arr))]

def coin_change_recurrsion(arr, i, t):
    if i < 0: return 0

    if i == 0:
        if t % arr[0] == 0:
            return 1

    if t == 0: return 1
    
    count = 0
    take = 0

    not_take = coin_change_recurrsion(arr, i - 1, t)
    if arr[i] <= t:
        take = coin_change_recurrsion(arr, i, t - arr[i])
    
    return take + not_take

# T(C) -> exponential
# S(C) -> O(t)

print(coin_change_recurrsion(arr, len(arr)-1, t))

def coin_change_dp(arr, i, dp, t):
    if i < 0: return 0

    if dp[i][t] != -1:
        return dp[i][t]

    if i == 0:
        if t % arr[0]:
            return 1
            
    if t == 0: return 1
    
    count, take = 0, 0

    not_take = coin_change_recurrsion(arr, i - 1, t)
    if arr[i] <= t:
        take = coin_change_recurrsion(arr, i, t - arr[i])
    
    dp[i][t] = take + not_take
    return dp[i][t]

# T(C) -> O(N * T)
# S(C) -> O(N * T) + O(N)
print(coin_change_dp(arr, len(arr)-1, dp, t))


def coin_change_tab(arr, i, t):
    dp = [[0] * (t + 1) for _ in range(len(arr))]

    for i in range(t + 1):
        if i % arr[0] == 0:
            dp[0][i] = 1

    for i in range(1, len(arr)):
        for j in range(t + 1):
            
            not_take = dp[i - 1][j]
            if arr[i] <= j:
                take = dp[i][j - arr[i]]
            else:
                take = 0
                
            dp[i][j] = take + not_take

    return dp[len(arr)-1][t]

# T(C) -> O(N * T)
# S(C) -> O(N * T)

print(coin_change_tab(arr, 0, t))

def coin_change_optimization(arr, i, t):
    prev = [0] * (t + 1)
    for i in range(t + 1):
        if i % arr[0] == 0:
            prev[i] = 1

    for i in range(1, len(arr)):
        curr = [0] * (t + 1)
        for j in range(t + 1):
            
            not_take = prev[j]
            take = 0
            if arr[i] <= j:
                take = curr[j - arr[i]]
                
            curr[j] = take + not_take

        prev = curr[:]

    return prev[t]

# T(C) -> O(N * T)
# S(C) -> O(T)
print(coin_change_optimization(arr, 0, t))



    


    
