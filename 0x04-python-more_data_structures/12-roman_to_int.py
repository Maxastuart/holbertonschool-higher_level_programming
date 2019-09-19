#!/usr/bin/python3
def roman_to_int(roman_string):
    result=0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    '''for each sequential letter in the string add it all up'''
    for c in roman_string:
        result += romans[c]
    for i, n in zip(roman_string, roman_string[1:]):
        if i < n:
            result -= i
    return result
