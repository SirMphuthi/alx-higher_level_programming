#!/usr/bin/python3
"""
A function that writes a string to text file
and returns total characters written
"""


def write_file(filename="", text=""):
    """The module for write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
