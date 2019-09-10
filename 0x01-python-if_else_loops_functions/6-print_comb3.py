#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            continue
        else:
            print('{}{}'.format(i, j), end="")
            if i < 8:
                print('', end=", ")
            else:
                print('')
