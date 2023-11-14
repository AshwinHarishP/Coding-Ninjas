def count_subsets_R(arr, k, i):
    if i < 0 or k < 0:
        return 0
    
    if k == 0:
        return 1

    if i == 0 and arr[0] == k:
        return 1

    count = 0

    count += count_subsets_R(arr, k - arr[i], i - 1)
    count += count_subsets_R(arr, k, i - 1)

    return count


def count_subsets_dp(arr, k, i, dp):
    if dp[i][k] != -1:
        return dp[i][k]

    if i < 0 or k < 0:
        return 0

    if k == 0:
        return 1
    
    if i == 0 and arr[0] == k:
        return 1

    count = 0

    count += count_subsets_dp(arr, k - arr[i], i - 1, dp)
    count += count_subsets_dp(arr, k, i - 1, dp)
    dp[i][k] = count

    return dp[i][k]


def count_subsets_tab(num, k):
    n = len(num)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = 1

    if arr[0] <= k:
        dp[0][num[0]] = 1

    for i in range(1, n):
        for j in range(1, k + 1):
            not_take = dp[i - 1][j]
            take = 0
            if num[i] <= j:
                take = dp[i - 1][j - num[i]]
            
            dp[i][j] = take + not_take

    return dp[n - 1][k]

def count_subsets_optimization(arr, k):
    prev = [0] * (k + 1)
    
    prev[0] = 1
    if arr[0] <= k:
        prev[arr[0]] = 1
    for i in range(1, len(arr)):
        curr = [0] * (k + 1)
        curr[0] = 1
        for j in range(1 , k + 1):
        
            take = 0
            if arr[i] <= j:
                take = prev[j - arr[i]]
            not_take = prev[j]

            curr[j] = take + not_take
        prev = curr[:]
    return curr[k]
            

arr = [1, 1, 4, 5]
k = 5


print(count_subsets_optimization(arr, k))

