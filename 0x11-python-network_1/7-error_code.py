#!/usr/bin/python3
"""
This module takes in a URL,
sends a request to the URL and displays the body of the response
"""
import sys
import requests
import requests.exceptions

if __name__ == "__main__":
    try:
        req = requests.get(url=sys.argv[1], allow_redirects=True)
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
