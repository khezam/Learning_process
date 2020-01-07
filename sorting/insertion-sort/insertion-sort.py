def swapping_nums(arr, i, cp):
	temp = arr[cp]
	arr[cp] = arr[i]
	arr[i] = temp
	return arr

def insertion_sort(arr):
	i = 1
	n = len(arr) - 1
	while i <= n:
		cp = i - 1
		if arr[i] < arr[cp]: 
			swapping_nums(arr, i, cp)
			# while cp is greater than 0(coming from the right side), then add 1 to cp which graps the previous element
			while cp > 0:
				subCp = cp - 1
				# if the previous elment of cp is greater than cp, than swap
				if arr[subCp] > arr[cp]:
					swapping_nums(arr, cp, subCp)
				cp -=1
		i +=1
	return arr
print(f'Input: [8, 3, 2, 9, 4, 7, 10, 6, 1, 5] Output: {insertion_sort([8, 3, 2, 9, 4, 7, 10, 6, 1, 5])}')	 
