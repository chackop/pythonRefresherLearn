import time
import random


def wait_game():
    target = random.randint(1, 5)
    print(f"Try to wait for {target} seconds without pressing Enter.")

    input("Press Enter to start waiting...")
    start_time = time.perf_counter()

    input("Press Enter after " + str(target) + " seconds to stop waiting...")
    end_time = time.perf_counter() - start_time

    print(f"You waited for {end_time:.2f} seconds.")

    if end_time == target:
        print("Perfect timing! You win!")
    elif end_time < target:
        print("You stopped too early! You lose!")
    else:
        print("You stopped too late! You lose!")


print(wait_game())  # Call the function to play the waiting game
