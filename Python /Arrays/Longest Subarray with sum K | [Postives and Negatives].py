from typing import List

def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) 
    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):

        Sum += a[i]

        if Sum == k:
            maxLen = max(maxLen, i + 1)

        rem = Sum - k

        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

if __name__ == "__main__":
    a = [-1, 1, 1]
    k = 1
    length = getLongestSubarray(a, k)
    print(f"The length of the longest subarray is: {length}")
