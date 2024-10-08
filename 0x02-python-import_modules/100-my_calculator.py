#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a. <operator> ,b.")
        sys.exit(1)

        func = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(func.keys()):
            print("Unknown operatot, Available operators: +, -, * and /")
            sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, func[sys.argv[2]](a, b)))
