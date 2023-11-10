
board = [[1, 2, 3], [4, 5, 4], [7, 5, 9]]
m, n = 3, 3
dp = [ [-1] * n for _ in range(m)]

def min_cost_recurrsion(m, n, board):
    if m == 0 and n == 0:
        return board[m][n]

    if m < 0 or n < 0:
        return float("inf")

    down =  board[m][n] + min_cost_recurrsion(m - 1, n, board)
    right = board[m][n] + min_cost_recurrsion(m, n - 1, board)

    return min(down, right)

def min_cost_dp(m, n, board, dp):
    if dp[m][n] != -1:
        return dp[m][n]

    if m == 0 and n == 0:
        return board[m][n]

    if m < 0 or n < 0:
        return float("inf")

    down = board[m][n] + min_cost_dp(m - 1, n, board, dp)
    right = board[m][n] + min_cost_dp(m, n - 1, board, dp)

    dp[m][n] = min(down, right)

    return dp[m][n]


def min_cost_tabulation(m, n, board, dp):
    for i in range(m):
        for j in range(n):

            if i == 0 and j == 0:
                dp[i][j] = board[0][0]

            else:
                down, right = float("inf"), float("inf")
                if i > 0: down = board[i][j] + dp[i - 1][j]
                if j > 0: right = board[i][j] + dp[i][j - 1]

                dp[i][j] = min(down, right)
    return dp[m-1][n-1]


def Space_optimizaion_minCost(m, n, board):
    prev = [0] * n
    for i in range(m):
        curr = [0] * n 
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = board[0][0]
            else:
                down, right = float("inf"), float("inf")
                if i > 0: down = board[i][j] + prev[j]
                if j > 0: right = board[i][j] + curr[j - 1]

                curr[j] = min(down, right)
        prev = curr

    return prev[n - 1]

print(Space_optimizaion_minCost(m, n, board))
