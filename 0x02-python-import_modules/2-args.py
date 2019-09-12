#!/usr/bin/python3
import sys
if __name__ == "__main__":
    print("{:d} argument".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print("s.")
    elif len(sys.argv) == 2:
        print(":")
        print("1: {}".format(sys.argv[1]))
    else:
        print("s:")
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
