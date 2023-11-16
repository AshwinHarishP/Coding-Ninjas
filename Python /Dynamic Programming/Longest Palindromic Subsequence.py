# n = len(s1) and m = len(s2)

s1 = "bbbab"
s2 = s1[::-1]
dp = [[-1] * (len(s1) + 1) for _ in range(len(s1) + 1)]
def Longest_palindrome_R(s1, s2, i, j):
    if i < 0 or j < 0:
        return 0

    if s1[i] == s2[j]:
        return 1 + Longest_palindrome_R(s1, s2, i - 1, j - 1)
    
    return max( (Longest_palindrome_R(s1, s2, i - 1, j)), (Longest_palindrome_R(s1, s2, i, j - 1)))


# T(C) -> O(Exponential)
# S(C) -> O(n * m)
print(Longest_palindrome_R(s1, s2, len(s1)-1, len(s2)-1))

def Longest_palindrome_dp(s1, s2, i, j, dp):
    if i == 0 or j == 0:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + Longest_palindrome_dp(s1, s2, i - 1, j - 1, dp)

    else:
        dp[i][j] = max(Longest_palindrome_dp(s1, s2, i - 1, j, dp),Longest_palindrome_dp(s1, s2, i, j - 1, dp))

    return dp[i][j]

# T(C) -> O(n * m)
# S(C) -> O(n * m) + O(n * m)
print(Longest_palindrome_dp(s1, s2, len(s1), len(s2), dp))

def Longest_palindrome_Tab(s1, s2, i, j):
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    
    for i in range(len(s1) + 1):
        dp[i][0] = 0

    for j in range(len(s2) + 1):
        dp[0][j] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]


# T(C) -> O(n * m)
# S(C) -> O(n * m)
print(Longest_palindrome_Tab(s1, s2, 0, 0))

def Longest_palindrome_Optimization(s1, s2, i, j):
    prev = [0] * (len(s1) + 1)
    
    for i in range(1, len(s1) + 1):
        curr = [0] * (len(s1) + 1)
        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]

            else:
                curr[j] = max(prev[j], curr[j - 1])
        
        prev = curr[:]

    return prev[len(s2)]

# T(C) -> O(n * m)
# S(C) -> O(m)
print(Longest_palindrome_Optimization(s1, s2, 0, 0))



