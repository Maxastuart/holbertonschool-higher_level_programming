#!/usr/bin/python3
import requests as r
from sys import argv
if __name__ == "__main__":
    try:
        j = r.get('https://api.github.com/user',
                  auth=(argv[1], argv[2])).json()
        print(str(j['id']))
    except:
        print("None")
