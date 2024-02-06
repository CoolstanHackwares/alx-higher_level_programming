#!/usr/bin/python3
"""Module 4-inherits_from.
Finds if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Determines if the obj is an instance of a class that
    inherits from a_class.

    Args:
        - obj: The object to look at
        - a_class: The class to evaluate

    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
