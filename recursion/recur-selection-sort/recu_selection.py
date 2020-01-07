def sorting(arr, i, h):
    if i >= h:
        return arr
    j = i
    curr = j
    while j < h:
        if arr[curr] > arr[j + 1]:
            curr = j + 1
        j += 1
    if curr != i:
        arr[i], arr[curr] = arr[curr], arr[i]
    return sorting(arr, i + 1, h)
sorting([10,2,9,8,7,6,5,4,3,1], 0, len([10,2,9,8,7,6,5,4,3,1]) - 1)