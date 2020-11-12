arr1 = [1, 2, 3, 4]
arr2 = [2, 5, 6]

m = len(arr1)
n = len(arr2)
t_length = m + n

# Unpack the array and fill in the 0 padded values
arr1 = [*arr1, *[0] * n]

p1 = m - 1
p2 = n - 1
p = t_length - 1

while p1 >= 0 and p2 >= 0:
    if arr1[p1] < arr2[p2]:
        arr1[p] = arr2[p2]
        p2 -= 1
    else:
        arr1[p] = arr1[p1]
        p1 -= 1

    p -= 1

arr1[:p2 + 1] = arr2[:p2 + 1]


print(arr1)
