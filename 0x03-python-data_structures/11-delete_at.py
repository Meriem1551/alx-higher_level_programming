#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list = my_list[:idx] + my_list[idx+1:]
    return my_list
