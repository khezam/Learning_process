"""I appying binary with recursion function"""
def binary_search_recursion(arr, target):
	"""A very important note: everytime that function gets called that arr get cut"""
	print(arr)
	if len(arr) == 0:
		return False
	else:
		midPoint = len(arr) // 2
		"""Try: int(len(arr) - 1) // 2 and comment out the line code above"""
		print(arr)
		if arr[midPoint] == target:
			return arr[midPoint]
		elif arr[midPoint] < target:
			return binary_search_recursion(arr[midPoint + 1:], target)
		else: 
			return binary_search_recursion(arr[:midPoint], targt)
	return None
# print(binary_search_recursion([1,2,3,4,5,6,7,8,9,10], 10)) 

"""Another way of doing it"""
def recur_binary(arr, start, end, target):
    if end <= 0 or start >= len(arr):
        return False
    half = (start + end) // 2
    if arr[half] == target:
        return arr[half]
    elif arr[half] < target:
        return recur_binary(arr, half + 1, end, target)
    else:
        return recur_binary(arr, start, half - 1, target)
        
# recur_binary([1,2,3,4,5,6,7,8,9,10], 0, len([1,2,3,4,5,6,7,8,9,10]), -1)

"""Another way of doing it"""
def rec_search(arr, start, end, h, target):
    if h <= 0:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return arr[mid] 
    elif arr[mid] < target:
        return search(arr, mid + 1, end, h // 2, target)
    else:
        return search(arr, start, mid - 1, h // 2, target)
# rec_search([1,2,3,4,5], 0, len([1,2,3,4,5]) - 1, len([1,2,3,4,5]) - 1, -1)


"""Another way of doing it"""
def rec_search(arr, start, end, target):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] < target:
        return rec_search(arr, mid + 1, end, target)
    else:
        return rec_search(arr, start, mid - 1, target)
# rec_search([1,2,3,4,5], 0, len([1,2,3,4,5]) - 1, -1) 