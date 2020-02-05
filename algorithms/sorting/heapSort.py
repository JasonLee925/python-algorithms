def heapify(arr, root, arr_length):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < arr_length and arr[largest] < arr[left]:
        largest = left
    if right < arr_length and arr[largest] < arr[right]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, largest, arr_length)


def heapSort(arr):
    # Build a maxheap
    for i in range(len(arr)-1, -1, -1):
        heapify(arr, i, len(arr))

    for i in range(len(arr)-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr


print(heapSort([23, 6, 4, 9, 12, 30, 57]))
