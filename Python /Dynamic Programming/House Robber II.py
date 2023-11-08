from os import *
from sys import *
from collections import *
from math import *

def houseRobber(valueInHouse):
    def House_robber(arr):
        prev1 = arr[0]
        prev2 = 0
        for i in range(1, len(arr)):
            take = arr[i]
            if i > 1:
                take += prev2
        
            not_take = 0 + prev1

            max_i = max(take, not_take)
            prev2 = prev1
            prev1 = max_i
        return prev1
    if len(valueInHouse) == 0: return(0)
    if len(valueInHouse) == 1: return(valueInHouse[0])
        
    max_amount_starting_from_first = House_robber(valueInHouse[:-1])

    
    max_amount_starting_from_second = House_robber(valueInHouse[1:])

    return max(max_amount_starting_from_first, max_amount_starting_from_second)
