#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while count < x:
        try:
            print(my_list[i], end=' ')
            count += 1
            i += 1
        except IndexError:
            # Break the loop if the list index is out of range
            break
    print()  # New line after printing the elements
    return count
