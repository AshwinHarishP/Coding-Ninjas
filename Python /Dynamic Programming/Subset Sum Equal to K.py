arr = [1, 3, 2] 
k = 3
dp = [[False] * (k + 1) for _ in range(len(arr))]

def subsets_r(arr, k, i):
    if k == 0:
        return True
    if i == 0 and arr[i] == k:
        return True

    if i < 0 or k < 0:
        return False

    take = subsets_r(arr, k - arr[i], i - 1)
    not_take = subsets_r(arr, k, i - 1)

    return take or not_take


def subsets_dp(arr, k, i, dp):
    if dp[i][k] != -1:
        return dp[i]

    if k == 0:
        return True
    if i == 0 and arr[i] == k:
        return True

    if i < 0 or k < 0:
        return False

    take = subsets_r(arr, k - arr[i], i - 1)
    not_take = subsets_r(arr, k, i - 1)
    dp[i][k] = take or not_take

    return dp[len(arr)-1][k]

def subsets_tab(arr, k, i, dp):
    for i in range(len(arr)):
        dp[i][0] = True

    dp[0][arr[0]] = True

    for i in range(1, len(arr)):
        for j in range(1, k + 1):
            not_take = dp[i - 1][j]
            take = False
            if arr[i] <= j:

                take = dp[i - 1][j - arr[i]]
           
            dp[i][j] = take or not_take

    return dp[len(arr)-1][k]



def subsets_space_opt(arr, k, i):
    prev = [False] * (k + 1)
    curr = [False] * (k + 1)
    
    prev[0] = curr[0] = True
    

    prev[arr[0]] = True

    for i in range(1, len(arr)):
        for j in range(1, k + 1):
            not_take = prev[j]
            take = False
            if arr[i] <= j:

                take = prev[j - arr[i]]
           
            curr[j] = take or not_take

        prev = curr[:]

    return prev[k]

print(subsets_space_opt(arr, k, len(arr)-1))
