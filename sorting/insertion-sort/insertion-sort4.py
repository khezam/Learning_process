def insertion_sort(arr):
	n = len(arr)
	i = 1
	while i < n:
		j = i - 1
		while j > -1 and arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
			j -= 1
		i += 1
	return arr
print(insertion_sort([10,9,8,7,6,5,4,3,2,1]))
