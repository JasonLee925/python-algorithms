def selectionSort(arr):
    arr_length = len(arr)
    sorted = []
    while len(sorted) != arr_length:
        min_index = 0
        for i in range(len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        swap(arr, 0, min_index)
        sorted.append(arr[0])
        arr.pop(0)
    return sorted


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


print(selectionSort([23, 6, 4, 9, 12, 30, 57]))
