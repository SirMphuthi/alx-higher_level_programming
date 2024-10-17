#!/usr/bin/python3
"""
MyList class function
"""


class MyList(list):
    """A subclass of list that can print itself sorted."""

    def print_sorted(self):    
        """Prints a sorted version on the list"""
        print(sorted(self))
