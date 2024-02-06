#!/usr/bin/python3
"""Returns an object (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Returns the object represented by my_str.

    Args:
        - my_str: The JSON string representation

    Returns: The corresponding object
    """

    return json.loads(my_str)
