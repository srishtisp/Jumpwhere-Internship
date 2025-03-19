def kth_largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]