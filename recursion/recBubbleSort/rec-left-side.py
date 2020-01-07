def rec_bubbleSort(arr, h):
	if h <= 0:
		return
	rec_bubbleSort(arr, h - 1)

	n = len(arr) - h
	i = 0
	while i < n:
		if arr[i] > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
		i += 1
	return arr
# print(rec_bubbleSort([10,9,8,7,6,5,4,3,2,1], len([10,9,8,7,6,5,4,3,2,1]) - 1))

"""Another way of rec bubble sort"""
def bubble(arr, h):
    if h <= 0:
        return 
    i = 0
    while i < h:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1
    bubble(arr, h - 1)
    
    return arr

# bubble([10,9,8,7,6,5,4,3,2,1], len([10,9,8,7,6,5,4,3,2,1]) - 1)

"""Another way of rec bubble sort"""
def bubble(arr, h):
    if h <= 0:
        return arr
    i = 0
    while i < h:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1
    return bubble(arr, h - 1)

# bubble([10,9,8,7,6,5,4,3,2,1], len([10,9,8,7,6,5,4,3,2,1]) - 1)