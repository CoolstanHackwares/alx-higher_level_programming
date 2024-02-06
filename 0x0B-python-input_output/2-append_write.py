#!/usr/bin/python3
"""Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        - filename: The name of the file
        - text: The text to append

    Returns: The number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
