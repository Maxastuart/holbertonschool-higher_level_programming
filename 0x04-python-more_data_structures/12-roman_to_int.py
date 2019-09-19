#!/usr/bin/python3
def roman_to_int(roman_string):
    result=0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) is None:
        return
    elif len(roman_string) == 1:
        return romans[roman_string]
    '''make a list of each letter in the string and the one following it'''
    for i, n in zip(roman_string, roman_string[1:]):
        if romans[i] >= romans[n]:
            result += romans[i]
        else:
            result -= romans[i]
    '''add the last letter of the string which couldn't be zip'd'''
    result += romans[roman_string[-1]]

    return result
