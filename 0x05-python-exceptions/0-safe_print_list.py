#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    while True:
        try:
            if ret < x:
                print(my_list[ret], end='')
                ret += 1
            else:
                print()
                return ret
        except IndexError:
            print()
            return ret
