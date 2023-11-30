#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 add, sub, mul, div
    num_args = len(sys.argv) - 1
    if num_args != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] != "+" and sys.argv[2] != "-" and sys.argv[2] != "*" and sys.argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
