import secrets


def generate_password(num_words, wordlist_path="words.txt"):

    with open(wordlist_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[
            2:7778
        ]  # Skip the first two lines and limit to 7776 words

    word_list = [line.split()[1] for line in lines]  # Extract the second column (words)

    # Generate a random password
    passwordgen = "".join(secrets.choice(word_list) for _ in range(num_words))

    return passwordgen


generated_password = generate_password(12)
print("Generated Password:", generated_password)
