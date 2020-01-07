def swapItems(arr):
	subPointer = 0
	subLoopCount = len(arr) - 1
	while subPointer < subLoopCount:
		cp = subPointer + 1
		if arr[subPointer] > arr[cp]:
			temp = arr[cp]
			arr[cp] = arr[subPointer]
			arr[subPointer] = temp
		subPointer += 1
	return arr


def bubbleSort(arr):
	loopCount = len(arr) - 1
	i = 0
	while i < loopCount:
		swapItems(arr)
		i += 1
	return arr
print(f'This is the input [1, 3, 4, 6, 2, 9]')
print(f'This is the output {bubbleSort([1, 3, 4, 6, 2, 9])}')
