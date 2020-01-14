#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(
        urllib.request.Request(
            sys.argv[1],
            urllib.parse.urlencode(
                {'email': sys.argv[2]}).encode('ascii'))) as r:
        print(r.read().decode('utf-8'))
