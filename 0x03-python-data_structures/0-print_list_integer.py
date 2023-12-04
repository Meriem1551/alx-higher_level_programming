#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        i = 0
        for n in my_list:
            print("{:d}".format(n))
            i += 1
            if i != my_list.len():
                print("\n")
