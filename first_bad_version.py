def isBadVersion(mid):
    return 1


def first_bad_version(n: int):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
