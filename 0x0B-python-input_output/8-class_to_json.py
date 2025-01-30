#!/usr/bin/python3
"""Defines a function that returns a dictionary with a data structure
"""


def class_to_json(obj):
    """Module class_to_json
        returns a dictionary
    """
    return obj.__dict__
