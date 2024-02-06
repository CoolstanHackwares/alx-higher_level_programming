#!/usr/bin/python3
"""Module 1-my_list.
This creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList inherits from the list."""

    def print_sorted(self):
        """Prints the list, in ascending order."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
