#!/usr/bin/python3

def uppercase(str):
    new_str = ""

    for char in str:
        if ord(char) > 64 and ord(char) < 91:
            new_str += char
        elif ord(char) > 96 and ord(char) < 123:
            new_str += chr(ord(char) - 32)
        else:
            new_str += char

print("{}".format(new_str))
