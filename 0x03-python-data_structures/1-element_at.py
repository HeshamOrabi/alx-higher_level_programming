#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        print("None")
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))
