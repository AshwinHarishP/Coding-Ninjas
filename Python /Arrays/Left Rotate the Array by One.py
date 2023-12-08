def solve(arr, n):
    temp = arr[0]  
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  
    for i in range(n):
        print(arr[i], end=" ")

n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)
