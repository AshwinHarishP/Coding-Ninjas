wt_arr = [5, 10, 20]
cost_arr = [7, 2, 4]
tot_wt = 15

dp = [[-1] * (tot_wt + 1) for _ in range(len(wt_arr))]
def knapsack_R(wt_arr, cost_arr, tot_wt, i):
    if i == 0:
        if wt_arr[0] <= tot_wt:
            return (tot_wt // wt_arr[0]) * cost_arr[0]

        return 0

    not_take = knapsack_R(wt_arr, cost_arr, tot_wt, i - 1)
    take = 0
    if wt_arr[i] <= tot_wt:

        take = cost_arr[i] + knapsack_R(wt_arr, cost_arr, tot_wt - wt_arr[i], i)

    return max(take, not_take)

# T(C) -> exponential
# S(C) -> O(Total_weight)

print(knapsack_R(wt_arr, cost_arr, tot_wt, len(wt_arr)-1))

def knapsack_DP(wt_arr, cost_arr, tot_wt, i, dp):

    if i == 0:
        if wt_arr[0] <= tot_wt:
            return (tot_wt // wt_arr[0]) * cost_arr[0]
        return 0

    if dp[i][tot_wt] != -1:
        return dp[i][tot_wt]

    not_take = knapsack_R(wt_arr, cost_arr, tot_wt, i - 1)
    take = 0

    if wt_arr[i] <= tot_wt:
        take = cost_arr[i] + knapsack_R(wt_arr, cost_arr, tot_wt - wt_arr[i], i)

    dp[i][tot_wt] = max(take, not_take)

    return dp[i][tot_wt]

# T(C) -> O(N * Total_weight)
# S(C) -> O(N * Total_weight) + O(N)

print(knapsack_DP(wt_arr, cost_arr, tot_wt, len(wt_arr)-1, dp))

def knapsack_Tab(wt_arr, cost_arr, tot_wt, i):
    dp = [[0] * (tot_wt + 1) for _ in range(len(wt_arr))]

    for i in range(wt_arr[0], tot_wt + 1):
        dp[0][i] = ((i // wt_arr[0]) * cost_arr[0])

    for i in range(1, len(wt_arr)):
        for j in range(tot_wt + 1):
            
            not_take = dp[i - 1][j]
            take = 0

            if wt_arr[i] <= j:
                take = cost_arr[i] + dp[i][j - wt_arr[i]]

            dp[i][j] = max(take, not_take)

    return dp[len(wt_arr)-1][tot_wt]

# T(C) -> O(N * Total_weight)
# S(C) -> O(N * Total_weight)

print(knapsack_Tab(wt_arr, cost_arr, tot_wt, 0))

def knapsack_Optimization(wt_arr, cost_arr, tot_wt, i):
    prev = [0] * (tot_wt + 1)
    for i in range(wt_arr[0], tot_wt + 1):
        prev[i] = ((i // wt_arr[0]) * cost_arr[0])

    for i in range(1, len(wt_arr)):
        curr = [0] * (tot_wt + 1)
        for j in range(tot_wt + 1):
            
            not_take = prev[j]
            take = 0

            if wt_arr[i] <= j:
                take = cost_arr[i] + curr[j - wt_arr[i]]

            curr[j] = max(take, not_take)
        prev = curr[:]

    return prev[tot_wt]

# T(C) -> O(N * Total_weight)
# S(C) -> O(Total_weight)

print(knapsack_Optimization(wt_arr, cost_arr, tot_wt, 0))


    
