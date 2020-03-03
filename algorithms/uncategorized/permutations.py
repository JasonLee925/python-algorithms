def permutations(arr, visited):
    if len(arr) <= 1:
        print visited + [arr[0]]
        return
    for i in arr:
        new_arr = arr[:]
        new_arr.remove(i)
        permutations(new_arr, visited[:] + [i])
    return


permutations(['A', 'B', 'C', 'D'], [])
