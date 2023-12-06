#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    sorted_dict = a_dictionary
    for key in sorted_keys:
        print("{}: {}".format(key, sorted_dict[key]))
