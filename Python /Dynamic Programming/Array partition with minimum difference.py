from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    totalSum = sum(arr)
    prev = [False] * (totalSum + 1)
    
    
    prev[0] = True
    
    if arr[0] <= totalSum:

        prev[arr[0]] = True

    for i in range(1, len(arr)):
        curr = [False] * (totalSum + 1)
        curr[0] = True
        
        for j in range(1, totalSum + 1):
            not_take = prev[j]
            take = False
            if arr[i] <= j:

                take = prev[j - arr[i]]
           
            curr[j] = take or not_take

        prev = curr[:]

    mini = int(1e8)
    for i in range((totalSum // 2) + 1):
        if prev[i]:
            diff = abs(i - (totalSum - i))
            mini = min(mini, diff)
    return mini
