#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) > 64 and ord(char) < 91:
            print("{}".format(char))
        elif ord(char) > 96 and ord(char) < 123:
            print("{}".format(chr(ord(char) - 32)))
