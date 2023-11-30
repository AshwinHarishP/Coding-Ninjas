def check(s1, s2):
    if len(s1) != len(s2) + 1:
        return False

    first, second = 0, 0
    inserted = False  

    while second < len(s2):
        if s1[first] == s2[second]:
            first += 1
            second += 1
        elif not inserted:
            inserted = True
            first += 1
        else:
            return False

    return True

def longest_string(arr):
    n = len(arr)
    dp = [1] * n
    maxi = -1

    for i in range(n):
        for prev_index in range(i):
            if check(arr[i], arr[prev_index]) and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
            
        if dp[i] > maxi:
            maxi = dp[i]

    return maxi
arr = ["a", "b", "ba", "bca", "bda", "bdca"]
arr = sorted(arr, key = lambda x: len(x))
print(longest_string(arr))

# T(C) -> O(n^2)
# S(C) -> O(n)
