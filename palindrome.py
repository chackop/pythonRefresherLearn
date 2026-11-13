import re


def palindrome(s):
    forwards = "".join(re.findall(r"\w", s.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(palindrome("racecar"))  # True
