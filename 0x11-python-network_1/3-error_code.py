#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: " + str(e.code))
