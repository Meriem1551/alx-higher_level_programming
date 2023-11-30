#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_args = 0
    num_args = len(sys.argv) - 1
    if num_args == 0:
        sum_args = 0
    else:
        for i in range(1, num_args + 1):
            sum_args += int(sys.argv[i])
    print("{:d}".format(sum_args))
