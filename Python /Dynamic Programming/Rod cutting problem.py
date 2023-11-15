price = [3, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
dp = [[-1] * (n + 1) for _ in range(len(price))]

def rod_cutting_R(price, i, n):
    if i == 0:
        return n * price[0]

    not_take = rod_cutting_R(price, i - 1, n)
    take = 0
    if i + 1 <= n:
        take = price[i] + rod_cutting_R(price, i, n -(i + 1))

    return max(take, not_take)

# T(C) -> O(exponential)
# S(C) -> O(n)
print(rod_cutting_R(price, len(price)-1, n))

def rod_cutting_dp(price, i, n, dp):

    if i == 0:
        return n * price[0]

    if dp[i][n] != -1:
        return dp[i][n]

    not_take = rod_cutting_R(price, i - 1, n)
    take = 0
    if i + 1 <= n:
        take = price[i] + rod_cutting_R(price, i, n -(i + 1))

    dp[i][n] = max(take, not_take)

    return dp[i][n]

# T(C) -> O(n x n)
# S(C) -> O(n x n) + O(n)
print(rod_cutting_dp(price, len(price)-1, n, dp))

def rod_cutting_tab(price, i, n):
    dp = [[0] * (n + 1) for _ in range(len(price))]

    for i in range(n + 1):
        dp[0][n] = n * price[0]

    for i in range(1, len(price)):
        for j in range(n + 1):

            not_take = dp[i - 1][j]
            take = 0
            if i + 1 <= j:
                take = price[i] + dp[i][j -(i + 1)]

            dp[i][j] = max(take, not_take)

    return dp[len(price)-1][n]

# T(C) -> O(n x n)
# S(C) -> O(n x n)
print(rod_cutting_tab(price, 0, n))

def rod_cutting_optimization(price, i, n):
    prev = [0] * (n + 1)
    for i in range(n + 1):
        prev[i] = i * price[0]

    for i in range(1, len(price)):
        curr = [0] * (n + 1)
        for j in range(n + 1):

            not_take = prev[j]
            take = 0
            if i + 1 <= j:
                take = price[i] + curr[j -(i + 1)]

            curr[j] = max(take, not_take)

        prev = curr[:]

    return prev[n]

# T(C) -> O(n x n)
# S(C) -> O(n + m)
print(rod_cutting_optimization(price, 0, n))


def rod_cutting_optimization_2(price, i, n):
    prev = [0] * (n + 1)
    for i in range(n + 1):
        prev[i] = i * price[0]

    for i in range(1, len(price)):
        for j in range(n + 1):

            not_take = prev[j]
            take = 0
            if i + 1 <= j:
                take = price[i] + prev[j -(i + 1)]

            prev[j] = max(take, not_take)

    return prev[n]

# T(C) -> O(n x n)
# S(C) -> O(n)
print(rod_cutting_optimization_2(price, 0, n))


      
