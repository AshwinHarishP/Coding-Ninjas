def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    hash_arr = [0] * n

    for i in range(n):
        hash_arr[i] = i
        for prev_index in range(i):
            if arr[prev_index] < arr[i] and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
                hash_arr[i] = prev_index

    max_length = max(dp)
    last_index = -1

    for i in range(n):
        if dp[i] == max_length:
            last_index = i
            break

    i = max_length - 1
    
    lis = [arr[last_index]]
    while hash_arr[last_index] != last_index:
        last_index = hash_arr[last_index]
        lis.append(arr[last_index])

    return lis[::-1]


arr = [10, 9, 2, 5, 3, 7, 101, 188]
print(longest_increasing_subsequence(arr))
