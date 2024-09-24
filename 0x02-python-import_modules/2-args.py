#!/usr/bin/python3

def print_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.".format(n))
    elif n == 1:
        print("1 argument:".format(n))
    else:
        print("{:d} arguments:".format(n))
    for i in range(1, n + 1):
        print("{:d}: {:s}".format(i, argv[i]))

if __name__ == "__main__":


    import sys
    print_arg(sys.argv)
