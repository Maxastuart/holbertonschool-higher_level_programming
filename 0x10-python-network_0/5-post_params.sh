#!/bin/bash
# send header in curl GET request
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
