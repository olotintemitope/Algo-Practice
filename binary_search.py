def binary_search(haystack, needle):
    i = 0
    if len(haystack) > 1:
        low = 0
        high = len(haystack) - 1
        mid = int((low + high) / 2)

        for number in haystack:
            if needle < haystack[mid]:
                mid -= 1
            elif needle > haystack[mid]:
                mid += 1
            else:
                return haystack[mid]
            i += 1


found = binary_search([1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222], 155)

print("I found the number: {} in a few step".format(found))
