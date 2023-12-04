#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None
    n_max = my_list[0]
    for item in my_list:
        if item > n_max:
            n_max = item
    return n_max
    
