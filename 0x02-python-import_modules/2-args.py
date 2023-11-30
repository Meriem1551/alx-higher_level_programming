#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    if num_args == 1:
        print("0 arguments.")
    else:
        print("{:d} argument".format(num_args - 1), end="")
        if num_args > 2:
            print("s", end="")
            print(":")
            for i in range(1, num_args):
                print("{:d}: {:s}".format(i, sys.argv[i]))
