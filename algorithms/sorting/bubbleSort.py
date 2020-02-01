def bubbleSort(arr):
    arrLength = len(arr)
    sorted = []
    while len(sorted) != arrLength:
        if len(arr) > 1:
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    swap(arr, i, i + 1)
                if arr[i+1] == arr[len(arr) - 1]:
                    sorted.insert(0, arr[len(arr) - 1])
                    arr.pop()
        else:
            sorted.insert(0, arr[len(arr) - 1])
            arr.pop()
    return sorted


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


print(bubbleSort([5, 2, 3, 1, 9, 8]))
