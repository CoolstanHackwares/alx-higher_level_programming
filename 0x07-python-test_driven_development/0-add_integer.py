#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: first integer or float
    - b: second integer or float (default is 98)

    Returns:
    - Integer: the addition of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b

