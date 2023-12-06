#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    r_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    last_rom = 0
    for num in reversed(roman_string):
        value = r_nums[num]
        if last_rom > value:
            result -= value
        else:
            result += value
        last_rom = value
    return result
