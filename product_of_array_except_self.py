from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    dp = [0] * length
    dp[0] = 1

    for i in range(1, length):
        dp[i] = nums[i - 1] * dp[i - 1]

    R = 1
    for i in reversed(range(length)):
        dp[i] = dp[i] * R
        R *= nums[i]

    return dp


data = [1, 1, 1, 1, -1, 1, 5, 1, -1, -1, -1, 1, -1, 1, -3, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 5, -1, 1, -1, 1, 1, 3,
        -1, -5, -1, 1, -1, 1, -1, -3, 1, 2, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -3, -1, -1, 4, -1, 1, -1, 1,
        -1, -1, -1, -1, 3, 1, 4, -5, -1, 1, 1, 1, 1, 1, -4, 1, 1, -3, -1, -1, 1, 3, -1, 1, -2, 1, -1, 1, 1, 1, -1, 1, 1,
        1, -1]
data2 = [1, 2, 3, 4, 5]
print(productExceptSelf(data2))
