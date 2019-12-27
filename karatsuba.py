def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    num1_str = str(num1)
    num2_str = str(num2)
    mid = max(len(num1_str), len(num2_str)) / 2

    a = num1 // 10**(mid)
    b = num1 % 10**(mid)
    c = num2 // 10**(mid)
    d = num2 % 10**(mid)
    step1 = karatsuba(a, c)
    step2 = karatsuba(b, d)
    step3 = karatsuba((a+b), (c+d))
    step4 = step3 - step2 - step1
    return int(step1 * (10**(2 * mid)) + step2 + step4 * 10**(mid))


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))
