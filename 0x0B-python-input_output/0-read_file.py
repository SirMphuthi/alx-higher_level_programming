#!/usr/bin/python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """"Reads a text file and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
