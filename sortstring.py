def sortstring(s):
    return " ".join(sorted(s.split(), key=str.casefold))


print(sortstring("hello this is a test"))  # Output: " a hello is test this"
