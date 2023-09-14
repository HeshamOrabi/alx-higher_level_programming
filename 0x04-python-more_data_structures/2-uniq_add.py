#!/usr/bin/python3

def uniq_add(my_list=[]):
    dic = {}
    total = 0

    for i in my_list:
        if i not in dic:
            total += i
            dic[i] = True
    return total
