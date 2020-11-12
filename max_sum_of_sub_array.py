def max_sum_of_sub_array(lists, k):
    num = k
    list_length = len(lists)
    if list_length > 0:
        for i in range(0, list_length):
            if i > 0:
                k += 1
            sub_array = lists[i:k]
            if len(sub_array) == num:
                lists[i] = sum(sub_array)

    return max(lists)


print(max_sum_of_sub_array([2, 1, 5, 1, 3, 2], 3))

print(max_sum_of_sub_array([2, 3, 4, 1, 5], 2))
