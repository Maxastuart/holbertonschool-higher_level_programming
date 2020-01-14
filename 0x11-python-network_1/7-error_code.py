#!/usr/bin/python3
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: " + str(r.status_code))
