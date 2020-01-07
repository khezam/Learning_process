def binary_search(arr, target):
	first = 0
	last = len(arr) - 1 
	while first <= last:
		midpoint = (first + last) // 2
		print(midpoint)
		if arr[midpoint] == target:
			return midpoint 
		elif arr[midpoint] < target:
			first = midpoint + 1
		else: 
			last = midpoint - 1
	return None
binary_search([1,2,3,4,5,6,7,8,9,10], 10)