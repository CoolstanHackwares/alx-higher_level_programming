#!/usr/bin/python3
"""
Module 101-add_attribute
Defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible.

    Args:
        - obj: The object to add the attribute to
        - attribute: The name of the attribute to be added
        - value: The value of the attribute

    Raises:
        - TypeError: if the object cannot have a new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
