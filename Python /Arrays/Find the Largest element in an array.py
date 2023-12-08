def findLargestElement(arr, n):
    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max
