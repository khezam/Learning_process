def insertion_sort(arr):
	j = 1
	while j < len(arr) - 1:
		i = j - 1
		# A copy of the pointer
		# The reason why I have a copy of the pointer so I can decrement the copy of the pointer
		subj = j 
		# Coming from right to left 
		while i > -1:
			# if the copy of the pointer is less than the before the pointer 
			if arr[subj] < arr[i]:
				temp = arr[i]
				arr[i] = arr[subj]
				arr[subj] = temp
			i -=1
			subj -=1
		j +=1
	return arr
print(f'Input: [8, 4, 2, 5, 1, 9, 6, 3, 7] Output: {insertion_sort([8, 4, 2, 5, 1, 9, 6, 3, 7])}')
