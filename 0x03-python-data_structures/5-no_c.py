#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        return None
    for char in my_string:
        if char == 'c' or char == 'C':
            my_string = my_string.remove(char)
    return my_string
