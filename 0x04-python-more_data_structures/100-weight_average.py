#!/usr/bin/python3

def weight_average(my_list=[]):
    up = sum(item[0] * item[1] for item in my_list)
    down = sum(item[1] for item in my_list)
    return up / down if down != 0 else 0
