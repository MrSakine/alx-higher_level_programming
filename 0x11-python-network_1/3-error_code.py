#!/usr/bin/python3
"""
This module takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    try:
        req = urllib.request.Request(url=sys.argv[1])
        with urllib.request.urlopen(req) as data:
            print(data.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))
