#!/usr/bin/python3

def read_file(filename=""):
    """
    Function to read and print the contents of a text file.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:

        content = file.read()

        print(content, end='')

if __name__ == "__main__":

    read_file("my_file_0.txt")
