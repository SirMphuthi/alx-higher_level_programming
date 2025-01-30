#!/usr/bin/python3
"""Defines a function that returns an object by a JSON string"""

import json


def from_json_string(my_str):
    """Module from_json_string
    returns Python object
    """
    return json.loads(my_str)
