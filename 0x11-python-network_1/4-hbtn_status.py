#!/usr/bin/python3
import requests
if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: " + str(type(r.text)))
    print("\t- content: " + str(r.text))
