#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers)

    while low < high:
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) \
                and (mid == len(list_of_integers) - 1 or \
                     list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid
        else:
            low = mid + 1
    return None
