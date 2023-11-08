from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    def subsequence(arr, n, dp):
        if n < 0:
            return 0

        if n == 0:
            return arr[n]

        if dp[n] != -1:
            return dp[n]

        pick = arr[n] + subsequence(arr, n - 2, dp)
        not_pick = 0 + subsequence(arr, n - 1, dp)
        
        dp[n] =  max(pick, not_pick)
        return dp[n]
    
    dp = [-1] * (len(nums))
    return subsequence(nums, len(nums) - 1, dp)


# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
