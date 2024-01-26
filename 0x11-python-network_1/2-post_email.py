#!/usr/bin/python3
"""
This module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    req_data = urllib.parse.urlencode({"email": sys.argv[2]})
    req_data = req_data.encode("ascii")
    req = urllib.request.Request(url=sys.argv[1], data=req_data)
    with urllib.request.urlopen(req) as data:
        print(data.read().decode("utf-8"))
