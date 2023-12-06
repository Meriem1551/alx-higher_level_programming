#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                my_list[j] = 0
    for i in range(len(my_list)):
        result += my_list[i]
    return result
