def selection(arr):
	n = len(arr) - 1
	i = 0
	while i < n:
		j = i 
		smallVal = j 
		while j < n:
			if arr[smallVal] > arr[j + 1]:
				smallVal = j + 1
			j += 1
		if smallVal != i:
			arr[i], arr[smallVal] = arr[smallVal], arr[i]
		i += 1
	return arr
print(selection([10, 1, 4, 9, 2, 6, 3, 5, 7, 8]))
