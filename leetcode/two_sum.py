""" Given an array of integers, return indices of the two numbers such that they add up to a specific target. """
def two_sum(arr, target):
	j = 1
	while j < len(arr) - 1:
		i = j - 1
		while i > -1:
			if arr[j] + arr[i] == target:
				return "{} + {} = {}".format(arr[j], arr[i], target)
			i -=1
		j +=1
print(two_sum([2, 7, 11, 15], 9))
