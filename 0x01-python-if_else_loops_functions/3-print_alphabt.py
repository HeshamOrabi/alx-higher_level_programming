#!/usr/bin/python3

for l in range(97, 123):
    if chr(l) == 'q' or chr(l) == 'e':
        continue
    else:
        print("{}".format(chr(l)), end="")
