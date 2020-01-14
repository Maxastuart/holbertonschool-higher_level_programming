#!/usr/bin/python3
import requests as r
from sys import argv
if __name__ == "__main__":
    j = r.get(
        'https://swapi.co/api/people/', params={'search': argv[1]}).json()
    print("Number of results: " + str(j['count']))
    for result in j['results']:
        print(result['name'])
