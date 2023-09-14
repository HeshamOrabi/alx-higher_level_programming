#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for k, v in sorted(a_dictionary.items(), key=lambda iteam: iteam[0]):
        print("{}: {}".format(k, v))
