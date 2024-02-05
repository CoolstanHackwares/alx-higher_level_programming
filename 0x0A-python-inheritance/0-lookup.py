#!/usr/bin/python3
""" defines the list of available attributes and methods in an object
"""

def lookup(obj):
    """Returns the list of available attributes and methods.

     Args:
        - obj: The object to lookup
    """

    return dir(obj)
