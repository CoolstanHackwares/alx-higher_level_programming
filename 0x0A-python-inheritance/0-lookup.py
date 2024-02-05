#!/usr/bin/python3
def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj (any): The object to lookup

    Returns:
        list: A list object containing string names of available attributes

    """
    return dir(obj)
