def bubble_sort(lists):
    for num in range(len(lists) - 1, 0, -1):
        for index in range(num):
            if lists[index] > lists[index + 1]:
                swap = lists[index]
                lists[index] = lists[index + 1]
                lists[index + 1] = swap

    return lists


data = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(data))
