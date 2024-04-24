from typing import *

def factorialNumbers(n: int) -> List[int]:
    def helper(i, fact, res):
        if fact <= n:
            res.append(fact)
            helper(i+1, fact * (i+1), res)
            return res
    res = []
    return helper(1, 1, res)
