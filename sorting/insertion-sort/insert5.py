# [10,9,8,7,6,5,4,3,2,1]
def insertion(arr):
    n = len(arr) 
    i = 1
    while i < n:
        j = i 
        while j > 0 and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    return arr
insertion([10,9,8,7,6,5,4,3,2,1])