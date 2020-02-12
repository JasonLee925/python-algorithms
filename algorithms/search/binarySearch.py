def binarySearch(arr, target, start, end):
    mid = (start+end) / 2

    if arr[mid] == target:
        return mid
    elif mid == start == end and arr[mid] != target:
        return None
    elif target > arr[mid]:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid)


data = [1, 4, 5, 7, 8, 11, 15, 23, 31,
        56, 77, 82, 93, 101, 200, 214, 579, 682, 1031]

print(binarySearch(data, 77, 0, len(data)-1))
