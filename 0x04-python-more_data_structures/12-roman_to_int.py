#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    eq_int = 0

    for r in reversed(roman_string):
        tmp = dic[r]
        eq_int += tmp if eq_int < tmp * 5 else -tmp
    return eq_int
