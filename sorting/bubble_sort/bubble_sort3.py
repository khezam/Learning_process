def bubble_sort(arr):
    n = len(arr) - 1
    while n:
        i = 0
        while i < n and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        n -= 1
    return arr
bubble_sort([10,9,8,7,6,5,4,3,2,1])