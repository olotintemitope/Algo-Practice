import re


def valid_palindrome(s: str):
    """write a regex to get all alphanumerics and spaces"""
    regex_pattern = r"[A-Za-z0-9]+"

    words_matched = re.findall(regex_pattern, s)
    converted_words_to_lowercase = "".join(words_matched).lower()

    return converted_words_to_lowercase == converted_words_to_lowercase[::-1]


print(valid_palindrome("aba"))
