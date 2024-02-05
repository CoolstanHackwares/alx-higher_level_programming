#!/usr/bin/python3
"""Module 0-lookup.
Finds the list of available attributes and methods of an object.
"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        - obj: The object to lookup
     """

    return dir(obj)
