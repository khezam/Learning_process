def bubble(arr, i, h):
        if i >= h:
            return arr
        j = h
        while j > i and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        return bubble(arr, i + 1, h)
bubble([10,9,8,7,6,5,4,3,2,1], 0, len([10,9,8,7,6,5,4,3,2,1]) - 1)