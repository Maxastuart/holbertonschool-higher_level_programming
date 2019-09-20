#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    current_roman_count = 0

    if len(roman_string) is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    for x in roman_string:
        if x not in romans:
            return 0
    if len(roman_string) == 1:
        return romans[roman_string]

    '''
    Make a list of each letter in the string and the one following it.
    If the current roman numeral is not I:1 and is repeated before a larger \
    roman numeral, return 0.
    '''
    for i, n in zip(roman_string, roman_string[1:]):

        if romans[i] > romans[n]:
            result += romans[i]
            current_roman_count = 0

        elif romans[i] is romans[n]:
            if current_roman_count > 1:
                return 0
            if romans[i] is not romans['I']:
                current_roman_count += 1
            result += romans[i]
            '''otherwise roman[i] < roman[n]'''
        else:
            if romans[i] is not romans['I']:
                if current_roman_count > 1:
                    return 0
            result -= romans[i]

    '''add the last letter of the string which couldn't be zip'd'''
    result += romans[roman_string[-1]]

    return result
