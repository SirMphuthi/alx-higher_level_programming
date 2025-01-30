#!/usr/bin/python3
"""Defines a function that appends files."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file.
    Arguments:
            filename (str): The name of tbe file.
            text (str): The string to append to file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
