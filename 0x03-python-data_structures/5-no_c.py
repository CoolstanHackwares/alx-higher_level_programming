#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for a in range(len(my_string)):
        if my_string[a] in 'cC':
            continue
        new_string += my_string[a]
    return new_string
