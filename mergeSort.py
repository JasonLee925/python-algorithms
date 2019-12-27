import math
def merge(arr1, arr2):
  c = []
  i = 0
  j = 0
  for k in range(len(arr1)+len(arr2)):
    if i<len(arr1) and j < len(arr2) and len(c) < len(arr1)+len(arr2):
      if arr1[i] < arr2[j]:
        c.append(arr1[i])
        i += 1
      else:
        c.append(arr2[j])
        j += 1
    elif i == len(arr1):
      c.append(arr2[j])
      j += 1
    else:
      c.append(arr1[i])
      i += 1
  return c

def mergeSort(arr):
  if len(arr) <= 2: 
    return merge(arr[:1], arr[1:])
  else: 
    mid = int(math.floor(len(arr) / 2))
    a = mergeSort(arr[:mid])
    b = mergeSort(arr[mid:])
    return merge(a, b)

print(mergeSort([2,3,5,9,1,4,7,6,8]))
