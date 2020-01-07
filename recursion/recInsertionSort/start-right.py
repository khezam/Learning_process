def recurInsert(arr, i, h):
      if -1 >= i:
          return arr
      j = i
      while j < h and arr[j] > arr[j + 1]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]
          j += 1
      return recurInsert(arr, i - 1, h)
recurInsert([10,9,8,7,6,5,4,3,2,1], len([10,9,8,7,6,5,4,3,2,1]) - 2, len([10,9,8,7,6,5,4,3,2,1]) - 1)