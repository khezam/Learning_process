"""Start from the right"""
def insertion(arr):
	n = len(arr) - 1
	i = n - 1
	while i > -1:
		j = i
		while j < n and (arr[j + 1] < arr[j]):
			arr[j + 1], arr[j] = arr[j], arr[j + 1]
			j += 1
		i -= 1
	return arr
print(insertion([10,9,8,7,6,5,4,3,2,1]))
