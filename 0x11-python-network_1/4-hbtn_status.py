#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    req = requests.get(
        url="https://alx-intranet.hbtn.io/status",
        allow_redirects=True
    )
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
