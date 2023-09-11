#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    end = len(my_list) - 1

    while my_list[end]:
        print("{}".format(my_list[end]))
        end--
