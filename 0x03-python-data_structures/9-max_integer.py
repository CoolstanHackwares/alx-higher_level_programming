#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for a in range(1, len(my_list)):
            if my_list[a] > max:
                max = my_list[a]
        return max
    return None
