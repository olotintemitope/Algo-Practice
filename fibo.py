def fibo_series(position):
    if position < 1:
        return position

    first = 0
    second = 1
    next_value = first + second

    for num in range(2, position - 1):
        first = second
        second = next_value
        next_value = first + second

    return next_value


print(fibo_series(10))


def dynamic_fibo_series(position):
    if position < 1:
        return position

    fibo = [num for num in range(0, position)]
    fibo[0] = 0
    fibo[1] = 1

    count = 2

    for num in range(2, position):
        fibo[count] = fibo[count - 1] + fibo[count - 2]
        count += 1

    return fibo


print(dynamic_fibo_series(10))


def recursive_fibo(position):
    if position == 0:
        return 0
    if position == 1:
        return 1

    return recursive_fibo(position - 1) + recursive_fibo(position - 2)


print(recursive_fibo(10))
