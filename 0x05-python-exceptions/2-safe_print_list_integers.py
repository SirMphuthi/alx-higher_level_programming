#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    data = num = 0
    while True:
        try:
            if data < x:
                print("{:d}".format(my_list[data]), end='')
                data += 1
                num += 1
            else:
                print()
                return num
        except (ValueError, TypeError):
            data += 1
