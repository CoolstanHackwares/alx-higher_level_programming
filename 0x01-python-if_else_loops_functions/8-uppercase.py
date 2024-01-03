#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print('')
