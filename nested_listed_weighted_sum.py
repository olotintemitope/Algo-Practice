def nested_listed_weighted_sum(nestedList, depth=1):
    sum_up = 0
    for num in nestedList:
        if isinstance(num, int):
            sum_up += num * depth
        if isinstance(num, list):
            sum_up += nested_listed_weighted_sum(num, depth + 1)

    return sum_up


print(nested_listed_weighted_sum([1, [4, [6]]]))
print(nested_listed_weighted_sum([[1, 1], 2, [1, 1]]))

# print(len([4, [6]]))
