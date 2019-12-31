import math

inversion = 0

def merge(arr1, arr2):
    c = []
    j = 0
    i = 0
    global inversion
    for k in range(len(arr1)+len(arr2)):
        if i < len(arr1) and j < len(arr2) and len(c) < len(arr1)+len(arr2):
            if arr1[i] < arr2[j]:
                c.append(arr1[i])
                i += 1
            else:
                c.append(arr2[j])
                inversion += len(arr1) - i
                j += 1
        elif i == len(arr1):
            c.append(arr2[j])
            j += 1
        else:
            c.append(arr1[i])
            i += 1
    return c


def countInversions(arr):
    if len(arr) <= 2:
        return merge(arr[:1], arr[1:])
    else:
        mid = int(math.floor(len(arr) / 2))
        a = countInversions(arr[:mid])
        b = countInversions(arr[mid:])
        return merge(a, b)


countInversions([2, 3, 5, 9, 1, 4, 7, 6, 8])
print(inversion)
