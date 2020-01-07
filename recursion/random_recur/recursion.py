"""First example without using recursion"""
print("Not using recursion")
def not_recursion(h):
	i = 0 
	while i < h:
		j = 0
		while j <= i:
			print("#", end="")
			j +=1
		i +=1
		print("\n")
not_recursion(5)

print("\n")
print("The function below used recursion")
def recursion(h):
	if h == 0:
		return
	recursion(h - 1)
	i = 0
	while i < h:
		print("#", end="")
		i +=1
	print("\n")
recursion(5)			

arr = [9, 5, 7, 2, 4, 6, 8, 1, 3]
n = len(arr) - 1
def bubbleSort(arr, n): 
  i = 0
  while i < n:
    if arr[i] > arr[i + 1]:
      arr[i],  arr[i + 1] = arr[i + 1], arr[i]
      print(arr)
    i +=1
  if n == 0:
    return
  else:
    bubbleSort(arr, n - 1)
  return arr
print(bubbleSort(arr, n))

# x = [5,4,3,2,1]
# n = len(x) - 1
# i = 0
# def rec(arr, i, n):
#   if i < n:
#     arr[i], arr[n] = arr[n], arr[i]
#     rec(arr, i+1, n-1)
#     print(arr)
# rec(x, i, n)