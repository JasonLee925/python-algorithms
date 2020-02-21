# Method 1 ( Use recursion )
def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print fibonacci_recursion(9)


# Method 2 ( Use Dynamic Programming )

def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            ans = a + b
            a, b = b, ans
        return ans


print fibonacci_dp(9)
