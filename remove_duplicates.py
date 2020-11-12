def remove_duplicates(lists):
    """
        Iterate over the list
        create a tmp variable to check if the next element is
        the same if yes, then drop it and continue
   bina :param lists:
    :return:
    """
    k = 1
    arr = []

    for i in range(len(lists)):
        k += 1
        sub_array = lists[i:k]
        if len(sub_array) > 1:
            if sub_array[0] != sub_array[1]:
                arr.append(sub_array[0])
        else:
            arr.append(sub_array[0])

    return arr


print(remove_duplicates([2, 2, 2, 11]))
