def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		midPoint = len(arr) // 2
		left = merge_sort(arr[:midPoint])
		right = merge_sort(arr[midPoint:])
		
		lst = []
		i = 0
		j = 0 

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				lst.append(left[i])
				i +=1
			else:
				lst.append(right[j])
				j +=1
		while i < len(left):
			lst.append(left[i])
			i +=1
		while j < len(right):
			lst.append(right[j])
			j +=1

        """The code below is anlternive of the second and third while loops"""
        # lst += left[i:]
        # lst += right[j:]

		return lst
# merge_sort([10,9,8,7,6,5,4,3,2,1])


"""Merge sort O(nlogn)"""
def merge(left, right):
    sorted = []
    i = 0
    j = 0
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted += left[i:]
    sorted += right[j:]
    
    return sorted
    
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)
# mergeSort([5,4,3,2,1])



"""Merge sort O(nlogn)"""
def recMerge(theSeq, first, last, tmpArray):
    if first == last:
        return
    else:
        mid = (first + last) // 2
        
        recMerge(theSeq, first, mid, tmpArray)
        recMerge(theSeq, mid+1, last, tmpArray)
        
        mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray)

def mergeVirtualSeq( theSeq, left, right, end, tmpArray ): 
    a=left 
    b = right
    m=0

    while a < right and b<end: 
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1 
        else :
            tmpArray[m] = theSeq[b]
            b += 1 
        m += 1

    while a < right : 
        tmpArray[m] = theSeq[a] 
        a += 1
        m += 1
    while b< end: 
        tmpArray[m] = theSeq[b] 
        b += 1
        m += 1
    for i in range(end - left): 
        theSeq[i+left] = tmpArray[i]

def mergeSort( theSeq ): 
    n = len( theSeq )
    tmpArray = [None] * n
    
    recMerge( theSeq, 0, n-1, tmpArray )
    return theSeq
# mergeSort([5,4,3,2,1])