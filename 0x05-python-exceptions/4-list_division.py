#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    my_list = []
    data = 0
    if list_length <= 0:
        print("out of range")
        return my_list
    while data < list_length:
        try:
            my_list.append(my_list_1[data] / my_list_2[data])
        except ZeroDivisionError:
            print("division by 0")
            my_list.append(0)
        except TypeError:
            print("wrong type")
            my_list.append(0)
        except IndexError:
            print("out of range")
            my_list.append(0)
        finally:
            data += 1
    return my_list
