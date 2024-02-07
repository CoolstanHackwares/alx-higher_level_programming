#!/usr/bin/python3
""" A function that creates an Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Creates an object from filename.

    Args:
        - filename: The name of the JSON file

    Returns: the object
    """

    with open(filename, 'r') as f:
        return json.load(f)
