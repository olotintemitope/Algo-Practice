def quick_sort(lists):
    lists_length = len(lists)

    if lists_length > 2:
        current_position = 0
        """ Partition the lists """
        for index in range(1, lists_length):
            pivot = lists[0]
            if lists[index] <= pivot:
                current_position += 1
                swap = lists[index]
                lists[index] = lists[current_position]
                lists[current_position] = swap
        """ End of partitioning """
        swap = lists[0]
        lists[0] = lists[current_position]
        lists[current_position] = swap

        left_sorted = quick_sort(lists[0:current_position])
        right_sorted = quick_sort(lists[current_position + 1:lists_length])

        lists = left_sorted + [lists[current_position]] + right_sorted

    return lists


print(quick_sort([1, 4, 21, 3, 9, 20, 25, 6, 21, 14]))


def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


print(QuickSort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
