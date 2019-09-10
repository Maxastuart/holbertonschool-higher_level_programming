#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            d = chr(ord(c) + ord('A') - ord('a'))
        else:
            d = c
        print(d.format(), end="")
    print("".format())
