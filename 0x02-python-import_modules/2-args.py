#!/usr/bin/python3

import sys

if __name__ == "__main__":

    lenght = len(sys.argv) - 1

    if lenght == 0:
        print("0 arguments.")
    elif lenght == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lenght))

    for iarg in range(lenght):
        print("{}: {}".format(iarg + 1, sys.argv[iarg] + 1))
