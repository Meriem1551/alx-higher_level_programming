#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
    print("1: " + sys.argv[1])
else:
    print("{:d} arguments:".format(num_args))
    for i in range(1, num_args):
        print(f"{i}: {sys.argv[i]}")
~                                                                                                                                           
~                                                                                                                                           
~                       
