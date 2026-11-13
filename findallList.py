def findAllList(lst, target):
    indexes = []
    for i, value in enumerate(lst):
        if value == target:
            indexes.append(i)
        elif isinstance(value, list):
            for j in findAllList(value, target):
                indexes.append(i + j)
    return indexes


print(findAllList([1, 2, 3, 2, 4, 2], 2))  # Output: [1, 3, 5]
