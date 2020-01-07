def insertion(arr, i, h):
    if i >= h:
        return arr
    j = i
    while j > 0:
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
    return insertion(arr, i + 1, h)
insertion([5,4,3,2,1], 1, len([5,4,3,2,1]))