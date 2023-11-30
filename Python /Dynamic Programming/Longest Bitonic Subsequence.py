def bitonic(arr):
    dp1 = [1 for _ in range(len(arr))] 
    maxi_dp1 = -1
    maxi_dp2 = -1
    maxi = 0

    # Largest Increasing Subsequence (LIS)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp1[i] < 1 + dp1[j]:
                dp1[i] = 1 + dp1[j]


    # Largest Decreasing Subsequence (LDS)
    dp2 = [1 for _ in range(len(arr))] 
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j] and dp2[i] < 1 + dp2[j]:
                dp2[i] = 1 + dp2[j]

        maxi = max(maxi, dp1[i] + dp2[i]-1)

    return maxi
    
    
arr = [1, 11, 2, 10, 4, 5, 2, 1]
print(bitonic(arr))

# T(C) -> O(n ^ 2)
# S(C) -> O(n)
