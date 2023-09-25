#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for i in range(0, x):
        count += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
    print()
    return count
