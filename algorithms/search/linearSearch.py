def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linearSearch([23, 6, 4, 9, 12, 30, 57, 101, 73, 98], 57))
