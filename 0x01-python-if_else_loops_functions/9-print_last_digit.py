#!/usr/bin/pythoni3
def print_last_digit(number):
    if number < 0:
        number = -number
        return -(number % 10)
    else:
        return number % 10
