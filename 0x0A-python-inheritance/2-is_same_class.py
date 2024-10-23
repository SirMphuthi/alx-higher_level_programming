i#!/usr/bin/python3
"""Define a class_checking function."""


def is_same_class(obj, a_class):
    """Checks if am object is an instance of a given class.

    Arguments:
            obj (any): The object to check.
            a_class (type): The class to match the type of obj to.
    Returns:
        if obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) is a_class:
        return True
    return False
