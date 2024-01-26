#!/usr/bin/python3
"""
This module takes in a URL,
sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(url=sys.argv[1], allow_redirects=True)
    print(req.headers.get("X-Request-Id"))
