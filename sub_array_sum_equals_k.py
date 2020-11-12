import math
from typing import List
import csv


def read_test_cases():
    with open("test_cases.txt", newline='') as test_cases:
        test_cases = csv.reader(test_cases.readlines(), delimiter=',')

    return test_cases


def subarraySum(nums: List[int], k: int) -> int:
    list_length = len(nums)
    count = 0
    if list_length > 0:
        for i in range(0, list_length):
            sums = 0
            for j in range(i, list_length):
                sums += int(nums[j])
                if sums == k:
                    count += 1

    return count


arr = [val for val in read_test_cases()]

print(subarraySum([1, 1, 1], 2))

print(math.inf)
