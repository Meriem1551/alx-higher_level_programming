#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    num = -number
    last_digit = -(num%10)
else:
    last_digit = number%10
msg = f"Last digit of {number:d} is {last_digit}"
if last_digit > 5:
    msg = msg + " and is greater than 5"
elif last_digit == 0:
    msg = msg + " and is 0"
elif last_digit < 6 and last_digit != 0:
    msg = msg + " and is less than 6 and not 0"
print(msg)
