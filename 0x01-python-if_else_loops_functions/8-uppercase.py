#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if char >= 97 and char <= 122:
            char = char - 32
            print("{}".format(chr(char)), end='')
    print("")
