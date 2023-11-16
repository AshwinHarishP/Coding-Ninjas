# Example usage:
s1 = "ABCD"
s2 = "ABCD"

def substring_Tab(s1, s2):
    dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    ans = 0

    for i in range(len(s1) + 1):
        dp[i][0] = 0
    for j in range(len(s2) + 1):
        dp[0][j] = 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    
    return ans

# O(T) -> O(s1 * s2)
# O(S) -> O(s1 * s2)
print(substring_Tab(s1, s2))

def substring_optimization(s1, s2):
    ans = 0
    prev = [0] * (len(s1)+1)
    

    for i in range(1, len(s1) + 1):
        curr = [0] * (len(s1)+1)
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]
                ans = max(ans, curr[j])
            else:
                curr[j] = 0
        prev = curr[:]
    
    return ans

# O(T) -> O(s1 * s2)
# O(S) -> O(s1)
print(substring_optimization(s1, s2))


