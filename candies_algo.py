from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    max_candy = max(candies)

    index = 0
    for candy in candies:
        candy_and_extra = candy + extra_candies
        if candy_and_extra < max_candy:
            candies[index] = False
        else:
            candies[index] = True
        index += 1

    return candies


print(kids_with_candies(candies=[4, 2, 1, 1, 2], extra_candies=1))
