# Method 1 ( Use Greedy Method )
def coinChange_greedy(num, coins_arr):
    result = {}
    for coin in coins_arr:
        result[coin] = 0

    if num in coins_arr:
        for coin in coins_arr:
            if coin == num:
                result[coin] = 1
    else:
        coins_arr = sorted(coins_arr, reverse=True)
        for coin in coins_arr:
            while num >= coin:
                result[coin] += 1
                num -= coin
    return result

print 'Method 1 =>', coinChange_greedy(36, [33, 24, 12, 5, 1])


# Method 2 ( Use Dynamic Programming )

def coinChange_dp(num, coins_arr):
    result = {}
    coins_arr = sorted(coins_arr)
    for i in range(num+1):
        result[i] = None
    for i in range(num+1):
        coin_index = 0
        if i == 0:
            result[i] = 0
        while coin_index < len(coins_arr) and coins_arr[coin_index] <= i:
            if not result[i] or result[i - coins_arr[coin_index]] + 1 < result[i]:
                result[i] = result[i - coins_arr[coin_index]] + 1
            coin_index += 1
    return result[num]


print 'Method 2 =>', coinChange_dp(36, [33, 24, 12, 5, 1])
