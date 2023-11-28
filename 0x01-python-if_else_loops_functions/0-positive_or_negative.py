#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(f"{number:d} is positive")
elif number < 0:
    print(f"{number:d} is negative")
else:
    print(f"{number:d} is zero")
