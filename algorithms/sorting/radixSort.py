def radixSort(arr):
    max_num = max(arr)
    current_place = 1
    while max_num / current_place > 0:
        bucket = [0] * 10
        for i in range(len(bucket)):
            bucket[i] = []
        output = [] * len(arr)
        for i in arr:
            if current_place <= 1:
                bucket[i % (current_place * 10)].append(i)
            else:
                bucket[(i // current_place) % current_place].append(i)

        for i in bucket:
            for j in i:
                output.append(j)
        arr = output
        current_place = current_place * 10
    return arr


print(radixSort([23, 6, 4, 9, 12, 30, 57, 101, 201]))
