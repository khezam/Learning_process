def bubble_sort(arr):
	"""This function is O(n^2)"""
	n = len(arr) - 1
	i = 0
	"""For every iteration of the parent iterator subtract 1 from the len of arr"""
	while i < n:
		j = 0
		while j < n - i:
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
			j += 1
		i += 1
	return arr

def linear_bubble_sort():
	"""This function is the best case of bubble sort O(n) since the array is already sorted"""
	arr = bubble_sort([10,9,8,7,6,5,4,3,2,1])
	n = len(arr) - 1
	i = 0
	while i < n:
		if arr[i] > arr[i + 1]:
			return "The array is not sorted yet"
		i += 1
	return arr
print(linear_bubble_sort())
