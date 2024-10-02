#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        data = a / b
        print("Inside result: {:.1f}".format(data))
    except (TypeError, ZeroDivisionError):
        data = None
        print("Inside result: {}".format(data))
    finally:
        return data
