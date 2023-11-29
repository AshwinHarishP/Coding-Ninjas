from bisect import bisect_left
def Lis_R(arr, i, prev):
    if i == len(arr):
        return 0

    not_take = 0 + Lis_R(arr, i + 1, prev)
    take = 0

    if arr[i] > arr[prev] or prev == -1:
        take = 1 + Lis_R(arr, i + 1, i)

    return max(not_take, take)

arr = [5, 4, 11, 13, 23, 8]
print(Lis_R(arr, 0, -1))

# S(C) -> O(n)
# T(C) -> O(2 * n)

def Lis_memo(arr, i, prev, dp):

    if i == len(arr):
        return 0

    if dp[i][prev + 1] != -1:
        return dp[i][prev + 1]

    not_take = 0 + Lis_R(arr, i + 1, prev)
    take = 0

    if arr[i] > arr[prev] or prev == -1:
        take = 1 + Lis_R(arr, i + 1, i)

    dp[i][prev + 1] = max(not_take, take)
    return dp[i][prev + 1]
    


dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr))]
print(Lis_memo(arr, 0, -1, dp))

# S(C) -> O(n * n)
# T(C) -> O(n * n) + O(n)


def Lis_tab(arr):
    dp = [1 for _ in range(len(arr))]
    maxi = 1
    take = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(1 + dp[j], dp[i])

        maxi = max(maxi, dp[i])

    return maxi

print(Lis_tab(arr))

# S(C) -> O(n)
# T(C) -> O(n * 2)


def binary_search_Lis(arr):
    length = 1
    temp = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            temp.append(arr[i])
            length += 1
        else:
            index = bisect_left(arr, arr[i])
            temp[index] = arr[index]

    return length

print(binary_search_Lis(arr))

# S(C) -> O(n)
# T(C) -> O(n * log(n))
