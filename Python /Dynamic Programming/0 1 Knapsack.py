w_arr = [3, 2, 4]
t_w = 6
cost_arr = [30, 40, 60]
dp = [[-1] * (t_w + 1) for _ in range(len(w_arr))]

def knapsack_Recurrsion(w_arr, cost_arr, t_w, i):
    if i == 0:
        if w_arr[i] <= t_w:
            return cost_arr[i]
        return 0

    not_tak = 0 + knapsack_Recurrsion(w_arr, cost_arr, t_w, i - 1)
    take = -1e8
    if w_arr[i] <= t_w:

        take = cost_arr[i] + knapsack_Recurrsion(w_arr, cost_arr, t_w - w_arr[i], i - 1)
    
    return max(not_tak, take)
    
print(knapsack_Recurrsion(w_arr, cost_arr, t_w, len(w_arr)-1))

def knapsack_DP(w_arr, cost_arr, t_w, i, dp):

    if i == 0:
        if w_arr[i] <= t_w:
            return cost_arr[i]
        return 0

    if dp[i][t_w] != -1:
        return dp[i][t_w]


    not_tak = 0 + knapsack_Recurrsion(w_arr, cost_arr, t_w, i - 1)
    take = -1e8
    if w_arr[i] <= t_w:

        take = cost_arr[i] + knapsack_Recurrsion(w_arr, cost_arr, t_w - w_arr[i], i - 1)
    
    dp[i][t_w] = max(not_tak, take)
    return dp[i][t_w]

print(knapsack_DP(w_arr, cost_arr, t_w, len(w_arr)-1, dp))


def knapsack_Tab(w_arr, cost_arr, t_w, i):
    dp = [[0] * (t_w + 1) for _ in range(len(w_arr))]
    for i in range(w_arr[0], t_w + 1):
        dp[0][i] = cost_arr[0]

    for i in range(1, len(w_arr)):
        for j in range(1, t_w + 1):


            not_tak = 0 + dp[i - 1][j]
            take = -1e8
            if w_arr[i] <= j:

                take = cost_arr[i] + dp[i - 1][j - w_arr[i]]
    
            dp[i][j] = max(not_tak, take)
    return dp[len(w_arr)-1][t_w]

print(knapsack_Tab(w_arr, cost_arr, t_w, 0))

def knapsack_Optimization(w_arr, cost_arr, t_w, i):
    prev = [0] * (t_w + 1)
    
    for i in range(w_arr[0], t_w + 1):
        prev[i] = cost_arr[0]

   
    
    for i in range(1, len(w_arr)):
        for j in range(t_w, -1, -1):

            not_tak = 0 + prev[j]
            take = -1e8
            if w_arr[i] <= j:

                take = cost_arr[i] + prev[j - w_arr[i]]
    
            prev[j] = max(not_tak, take)

    return prev[t_w]

print(knapsack_Optimization(w_arr, cost_arr, t_w, 0))

