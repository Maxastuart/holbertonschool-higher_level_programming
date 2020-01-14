#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    print("Body response:")
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        content = r.read()
        print("\t- type: " + str(type(content)))
        print("\t- content: " + str(content))
        print("\t- utf8 content: " + content.decode('utf-8'))
