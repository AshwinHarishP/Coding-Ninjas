def Lis_print(arr):
    dp = [1 for _ in range(len(arr))]
    hash_arr = list(range(len(arr)))


    for i in range(len(arr)):
        for j in range(i):
            if arr[i] % arr[j] ==  0 and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                hash_arr[i] = j

    ans = -1
    last_index = -1
    # Find the maximum length and its corresponding index
    for i in range(len(arr)):
        if dp[i] > ans:
            ans = dp[i]
            last_index = i

    # Reconstruct the divisible subset
    result = [arr[last_index]]

    while hash_arr[last_index] != last_index:
        last_index = hash_arr[last_index]
        result.append(arr[last_index])

    return result[::-1]


arr = [1, 16, 7, 8 ,4]
arr = sorted(arr)
print(Lis_print(arr))
