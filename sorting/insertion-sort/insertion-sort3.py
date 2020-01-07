def insertion_sort(arr):
	j = 1 
	while j < len(arr) - 1:
		# A hold of the current value that is being swapped
		current = arr[j]
		i = j - 1
		while i > -1:
			# If the current holded value is less the item before, then swap
			if current < arr[i]:
				arr[i + 1] = arr[i]
				arr[i] = current
			i -=1
		j +=1
	return arr
print(f'Input: [8,4 2, 5, 1, 9, 6, 3, 7] Output: {insertion_sort([8, 4, 2, 5, 1, 9, 6, 3, 7])}')
