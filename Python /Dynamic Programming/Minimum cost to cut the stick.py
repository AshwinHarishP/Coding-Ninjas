def min_cost(n, c, cuts):
    cuts = [0] + cuts + [n]
    cuts.sort()
    dp = [[0 for _ in range(c + 2)] for _ in range(c + 2)]

    def f_tab(i, j):

        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                
                if i > j:
                    continue

                mini = int(1e8)

                for ind in range(i, j + 1):
                    cost = cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]

                    mini = min(mini, cost)
                    dp[i][j] = mini

        return dp[1][c]

        # T(C) -> O(n ^ 3)
        # S(C) -> O(n ^ 2)

    return f_tab(1, c)

    def f_memo(i, j):
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        mini = int(1e8)

        for ind in range(i, j + 1):
            cost = cuts[j + 1] - cuts[i - 1] + f_memo(i, ind - 1) + f_memo(ind + 1, j)

            mini = min(mini, cost)
            dp[i][j] = mini

        return mini

    # T(C) -> O(n ^ 3)
    # S(C) -> O(n ^ 2)

    

    def f_R(i, j):
        if i > j:
            return 0

        if i > j:
            return cuts[j] - cuts[i - 1]

        mini = int(1e8)

        for ind in range(i, j + 1):
            cost = cuts[j + 1] - cuts[i - 1] + f_R(i, ind - 1) + f_R(ind + 1, j)

            mini = min(mini, cost)

        return mini

    # T(C) -> O(3 ^ n) -> exponential
    # S(C) -> O(n) 
    return f_memo(1, c)



cuts = [3, 5, 1, 4]
c = len(cuts)
n = 7
print(min_cost(n, c, cuts))
