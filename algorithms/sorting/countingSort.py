def countingSort(arr):
    max_num = max(arr)
    count = [0] * (max_num + 1)
    output = [] * len(arr)

    for i in arr:
        count[i] = count[i] + 1

    for i in range(len(count)):
        if count[i] > 0:
            for j in range(count[i]):
                output.append(i)

    return output


print(countingSort([23, 6, 4, 9, 12, 30, 57, 101, 12, 101]))
