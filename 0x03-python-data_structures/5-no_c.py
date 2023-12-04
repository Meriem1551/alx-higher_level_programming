#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        return None
    my_string = ''.join([char for char in my_string if char != 'c' or char != 'C'])
    return my_string
