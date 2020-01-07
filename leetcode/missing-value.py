def sorting_arr(arr):
	j = 1 
	while j < len(arr) - 1:
		i = j - 1
		cp = j 
		while i > -1:
			if arr[cp] < arr[i]:
				temp = arr[i]
				arr[i] = arr[cp]
				arr[cp] = temp
			i -=1
			cp -=1
		j +=1
	return arr
def missing_value(arr):
	new_arr = sorting_arr(arr)	
	j = 1
	i = 0
	while i < len(new_arr) -1:
		if new_arr[j] - 1 != new_arr[j - 1]:
			return new_arr[j] - 1
		j +=1
		i +=1
print(missing_value([1,2,3,4,5,6,8]))
