def longest_substring_with_k_distinct(str, k):
    if len(str) > 0:
        look_up = {}
        letters = [letter for letter in str]

        for letter in letters:
            look_up[letter] = 0

        for letter in letters:
            look_up[letter] += 1

    return look_up


print(longest_substring_with_k_distinct("araaci", k=2))
