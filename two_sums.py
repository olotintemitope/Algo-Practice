from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    look_up = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in look_up:
            look_up[num] = i
        else:
            return [look_up[n], i]


print(twoSum([1, 2, 3, 4, 6], 6))
