from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp = [0] * n

    def frog_jump(n, arr, dp):
        dp[0] = 0

        for i in range(1, n):
            left = dp[i - 1] + abs(arr[i] - arr[i - 1])

            if i > 1:
                right = dp[i - 2] + abs(arr[i] - arr[i - 2])
            else:

                right = float("inf")

            dp[i] = min(left, right)
        return dp[n - 1]
        
    return frog_jump(n, heights, dp)

    
    
