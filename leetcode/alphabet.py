import string

def encrypt(input):
  alphabet = list(string.ascii_lowercase)
  i = 0
  length = len(alphabet) - 1
  lst = []
  
  while i <= length:
    if alphabet[i] not in input:
        lst.append(alphabet[i])
    i +=1
    
  return input + ''.join(lst)
# print(encrypt('cat'))
"""TWo different ways"""
import string 

def binary(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if ord(arr[mid]) == target:
            arr.pop(mid)
            return arr
        elif ord(arr[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def keyInput(arr, string):
    length = len(string) - 1
    
    while 0 <= length:
        binary(arr, ord(string[length]))
        length -=1
    return string + "".join(arr)
# print(keyInput(list(string.ascii_lowercase), "cat"))     