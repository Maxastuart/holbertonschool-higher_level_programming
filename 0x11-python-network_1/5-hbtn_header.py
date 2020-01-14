#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    r = requests.head(sys.argv[1])
    print(str(r.headers['X-Request-Id']))
