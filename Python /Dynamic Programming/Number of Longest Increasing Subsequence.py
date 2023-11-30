from typing import List

def findNumberOfLIS(arr: List[int]) -> int:
    # write your code here
    def Lis_count(arr):
        dp = [1 for _ in range(len(arr))]
        count = [1 for _ in range(len(arr))]
        maxi = 1

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]

                    # it says it is new dont add
                    count[i] = count[j]
                elif arr[j] < arr[i] and 1 + dp[j] == dp[i]:
                    # it says it already exist. It is similar so add(increase the count)
                    count[i] += count[j]

            maxi = max(maxi, dp[i])

        res = 0
        for i in range(len(arr)):
            if dp[i] == maxi:
                res += count[i]
        return res


    return(Lis_count(arr))
