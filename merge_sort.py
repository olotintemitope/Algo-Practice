def merge_sort(lists):
    if len(lists) > 1:
        mid = len(lists) // 2

        left_array = lists[:mid]
        right_array = lists[mid:]

        """ We need to sort both the left and the right arrays
            recursively and merge them together
        """

        merge_sort(left_array)
        merge_sort(right_array)

        i, j, k = (0, 0, 0)

        while i < len(left_array) and j < len(right_array):
            if left_array[i] > right_array[j]:
                lists[k] = right_array[j]

                j += 1
            else:
                lists[k] = left_array[i]

                i += 1

            k += 1

        while i < len(left_array):
            lists[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            lists[k] = right_array[j]
            j += 1
            k += 1


data = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
merge_sort(data)

print(data)