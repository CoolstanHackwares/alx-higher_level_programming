#!/usr/bin/python3
"""Returns the JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj.

    Args:
        - my_obj: The string to represent

    Returns: The JSON representation
    """

    return json.dumps(my_obj)
