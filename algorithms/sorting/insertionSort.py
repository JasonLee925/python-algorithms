def insertionSort(arr):
    for i in range(len(arr)):
        if i > 0:
            current_key = arr[i]
            j = i - 1
            insert_pos = i
            while arr[j] > current_key and j >= 0:
                insert_pos = j
                j = j - 1
            arr.pop(i)
            arr.insert(insert_pos, current_key)
    return arr


print(insertionSort([23, 6, 4, 9, 12, 30, 57]))
