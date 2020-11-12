import re


def valid_palindrome_2(s: str):
    regex_pattern = r"[a-z]+"
    words_matched = re.findall(regex_pattern, s)
    s = "".join(words_matched)
    if s == s[::-1]:
        return True
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            check1 = s[low + 1:high + 1]
            check2 = s[low:high]
            return check1 == check1[::-1] or check2 == check2[::-1]

        low += 1
        high -= 1

    return True


print(valid_palindrome_2("cca"))  # bca ca a ab bc ca

