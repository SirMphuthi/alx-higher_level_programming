#!/usr/bin/python3
"""Defines a function that returns JSON file of an object (string)
"""

import json


def to_json_string(my_obj):
    """Defines a function that returns of JSON format."""
    return json.dumps(my_obj)
