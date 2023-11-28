#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if char >= 97 and char <= 122:
            char = char - 32
            print("{}".format(chr(char)), end='')
    print()
