import re
import collections


def unique_words(path):
    with open(path, "r", encoding="utf-8") as f:
        all_words = re.findall(r"[0-9a-zA-Z-']+", f.read())
        caps_words = [word.upper() for word in all_words]
        print(f"All words: {caps_words}")
        word_count = collections.Counter(caps_words)

        print(f"Word count: {word_count}")
        for word in word_count.most_common():
            print(f"{word[0]}: {word[1]}")


unique_words_result = unique_words("input.txt")
print(f"Unique words: {unique_words_result}")
