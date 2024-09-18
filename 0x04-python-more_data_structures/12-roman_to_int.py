#!/usr/bin/python3

def roman_to_int(roman_string):
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0

    if roman_string is None or roman_string is str:
        return 0

    for str_val in roman_string:
        if str_val in a_dict:
            result += a_dict[str_val]
    return result
