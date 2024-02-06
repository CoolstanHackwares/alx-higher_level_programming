#!/usr/bin/python3
"""Module 2-is_same_class.
This function checks if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """A function to determine if obj is an instance of a_class.

    Args:
        - obj: The object to look check
        - a_class: A class to verify the instance of

    Returns: True if obj is an instance of a_class,
    False otherwise
    """

    return True if type(obj) is a_class else False
