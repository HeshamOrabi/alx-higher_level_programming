#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    lenght = len(argv) - 1

    if lenght == 0:
        print("0 arguments.")
    elif lenght == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lenght))

    for iarg in range(0, lenght):
        print("{}: {}".format(iarg + 1, argv[iarg] + 1))
