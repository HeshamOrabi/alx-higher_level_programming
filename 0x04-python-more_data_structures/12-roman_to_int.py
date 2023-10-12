#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    eq_int = 0

    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and dic[roman_string[i]] < dic[roman_string[i + 1]]:
            eq_int -= dic[roman_string[i]]
        else:
            eq_int += dic[roman_string[i]]
    return eq_int
