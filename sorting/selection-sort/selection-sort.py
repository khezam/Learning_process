def swap_itmes(arr, i, j):
	temp = arr[j]
	arr[j] = arr[i]
	arr[i] = temp
	return arr

def smallestValue(arr, i):
	j = i
	minValue = i
	while j <= len(arr) - 1:
		if arr[j] < arr[minValue]:
			minValue = j
		j +=1
	return minValue

def selection_sort(arr):
	i = 0
	while i < len(arr) - 1:
		minValue = smallestValue(arr, i)
		swap_itmes(arr, i, minValue)
		i +=1
	return arr
print(f'We are peforming a selection sort. Input: [8, 3, 7, 9, 4, 5, 6, 1, 2] Output: {selection_sort([8, 3, 7, 9, 4, 5, 6, 1, 2])}')
