def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    Sum = maxLen = 0
    hashmap = dict()

    for i in range(len(arr)):
        Sum += arr[i]

        if Sum == 0:
            maxLen = max(maxLen, i+1)
        
        elif Sum in hashmap:
            maxLen = max(maxLen, i - hashmap[Sum])
        
        else:
            hashmap[Sum] = i

    return maxLen
