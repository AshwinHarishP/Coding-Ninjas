def canPartition(arr, n):
    
    totSum = sum(arr)
    if totSum % 2 != 0:
        return False
    else:
        k = totSum // 2

    def space_optimization(arr, k):
        prev = [False] * (k+1)
        curr = [False] * (k+1)
        prev[0] = curr[0] = True

        if arr[0] <= k:
            prev[arr[0]] = True

        for i in range(1, n):
            for j in range(1, k + 1):
                not_take = prev[j]
                take = False

                if arr[i] <= j: 
                    take = prev[j - arr[i]]
                curr[j] = take or not_take 

            prev = curr[:]

        return  prev[k]

    if(space_optimization(arr, k)):
        return True
    return False











