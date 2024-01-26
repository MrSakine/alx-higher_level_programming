#!/usr/bin/python3
"""
This module takes in a URL,
sends a request to the URL and displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(url=sys.argv[1], allow_redirects=True)
    if (req.status_code == 200):
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
