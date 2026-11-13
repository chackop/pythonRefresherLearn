from collections import Counter
from random import randint


def dicethrow(*dice, num_throws=1000):

    counts = Counter()
    for _ in range(num_throws):
        counts[tuple(randint(1, sides) for sides in dice)] += 1

    print(f"Counts of each combination: {counts}")

    for outcome in range(len(dice), sum(dice) + 1):
        print(f"Outcome {outcome}: {counts[outcome]} times")


dicethrow_result = dicethrow(6, 6, 6, num_throws=1000)
print(f"Dice throw result: {dicethrow_result}")
