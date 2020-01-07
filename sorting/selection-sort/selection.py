def selection_sort(arr):
	"""[9,2,6,1,7,4,5,8,3]"""
	n = len(arr) - 1
	i = 0
	while i < n:
		current = i
		j = i
		while j <= n:
			if arr[j] < arr[current]:
				current = j
			j +=1
		temp = arr[i]
		arr[i] = arr[current]
		arr[current] = temp
		i +=1
	return arr		
# print(selection_sort([9,2,6,7,1,4,5,8,3])) 

def selection(arr):
    n = len(arr) - 1
    i = 0
    while n > i:
        j = i
        curr = j 
        while j < n:
            if arr[curr] > arr[j + 1]:
                curr = j + 1
            j += 1
        if curr != i:
            arr[i], arr[curr] = arr[curr], arr[i]
        i += 1
    return arr 
# selection([10,2,4,9,1,6,3,5,7,8])