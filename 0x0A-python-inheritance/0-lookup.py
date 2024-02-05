#usr/bin/python3
"""A function that defines the list of available attributes and methods
in an object"""

def lookup(obj):
"""Args:
        obj: The object to lookup


Returns:
A list object containing string names
of available attributes"""

    return dir(obj)
