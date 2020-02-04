def quickSort(arr, left, right):
    if left >= right:
        return arr
    key = arr[left]
    left_pivot = left
    right_pivot = right
    while left_pivot < right_pivot:
        while arr[left_pivot] <= key and left_pivot < right:
            left_pivot = left_pivot + 1
        while arr[right_pivot] >= key and right_pivot > left:
            right_pivot = right_pivot - 1

        if left_pivot >= right_pivot:
            # swap
            arr[left], arr[right_pivot] = arr[right_pivot], arr[left]
            quickSort(arr, left, right_pivot - 1)
            quickSort(arr, right_pivot + 1, right)
        else:
            # swap
            arr[left_pivot], arr[right_pivot] = arr[right_pivot], arr[left_pivot]

    return arr


data = [20, 9, 100, 0, 201, 3, 11]
print(quickSort(data, 0, len(data) - 1))
