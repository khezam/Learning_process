def total(arr, sum, i, h):
    if i >= h:
        return sum 
    return total(arr, sum + arr[i], i + 1, h)
total([1,2,3,4,5], 0, 0, len([1,2,3,4,5]))