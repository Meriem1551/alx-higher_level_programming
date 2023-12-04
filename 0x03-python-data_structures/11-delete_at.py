#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    if idx == 0:
        my_list = my_list[1:]
    elif idx == len(my_list) - 1:
        my_list = my_list[:len(my_list) - 1]
    else:
        my_list = my_list[:idx] + my_list[idx+1:]
    return my_list
