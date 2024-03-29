#!/usr/bin/python3
"""Writes an Object to a text file,
using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to filename.

    Args:
        - my_obj: The object to write
        - filename: The file to write into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
