def add_binary(num1, num2):
    n = max(len(num1), len(num2))
    num1, num2 = num1.zfill(n), num2.zfill(n)
    carry = 0
    sum_string = ''
    for i in range(n - 1, -1, -1):
        if num1[i] == '1':
            carry += 1
        if num2[i] == '1':
            carry += 1

        if carry % 2 == 1:
            sum_string += str(1)
        else:
            sum_string += str(0)

        carry //= 2

    if carry == 1:
        sum_string += str(1)

    return sum_string[::-1]


print(add_binary("11", "1"))
