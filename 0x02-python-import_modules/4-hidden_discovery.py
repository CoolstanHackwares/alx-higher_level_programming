#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    list = dir()
    for i in range(0, len(list)):
        if list[i][0:2] != "__":
            print("{}".format(list[i]))
