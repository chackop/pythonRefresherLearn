import pickle


def save_dict(dictionary, filename):
    with open(filename, "wb") as f:
        pickle.dump(dictionary, f)


def load_dict(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)


test_dict = {"name": "Alice", "age": 30, "city": "New York"}
save_dict(test_dict, "test_dict.pkl")

loaded_dict = load_dict("test_dict.pkl")
print(loaded_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
