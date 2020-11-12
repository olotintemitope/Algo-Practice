def sub_array(lists, k):
    averages = []
    if len(lists) > 0:
        for i in range(0, len(lists)):
            if i > 0:
                k += 1
            sub__arrays = lists[i:k]
            if len(sub__arrays) >= 5:
                averages.append(sum(sub__arrays) / 5)

    return averages


print(sub_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
