#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{:d} argument".format(len(sys.argv) - 1), end="")
        if len(sys.argv) > 2:
            print("s", end="")
            print(":")
            for i in range(1, len(sys.argv)):
                print("{:d}: {:s}".format(i, sys.argv[i]))
