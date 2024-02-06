#!/usr/bin/python3
"""Module 3-write_file.
A function that writes in a text file.
"""


def write_file(filename="", text=""):
    """Writes text in filename.

    Args:
        - filename: The name of the file
        - text: The string to write in the file

    Returns: The number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)
