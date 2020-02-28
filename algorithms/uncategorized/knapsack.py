def knapsack(weight_limit, items):
    data = {}
    data[0] = 0
    items = sorted(items, reverse=True)
    for i in range(1, weight_limit+1):
        data[i] = None

    for i in range(1, weight_limit+1):
        current_items_index = 0
        max_value = None
        while current_items_index < len(items):
            if items[current_items_index][0] <= i:
                if not max_value or (items[current_items_index][1] + data[i - items[current_items_index][0]]) > max_value:
                    max_value = items[current_items_index][1] + \
                        data[i - items[current_items_index][0]]
            current_items_index += 1

        if max_value:
            data[i] = max_value
        else:
            data[i] = 0

    return data[weight_limit]


items = [[9, 8], [2, 1], [5, 3], [7, 9], [1, 1]]  # [w, v]
print knapsack(10, items)

items = [[10, 60], [20, 100], [30, 120]]
print knapsack(50, items)
