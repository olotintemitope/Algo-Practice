def findPairsWithGivenDifference(arr, k):
    # since we don't allow duplicates, no pair can satisfy x - 0 = y
    if k == 0:
        return []

    pair_map = {}
    answer = []

    for x in arr:
        pair_map[x - k] = x

    for y in arr:
        if y in pair_map:
            answer.append([pair_map[y], y])
    return answer


print(findPairsWithGivenDifference([0, -1, -2, 2, 1], 1))
