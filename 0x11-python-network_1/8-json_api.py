#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.post(
        url="http://0.0.0.0:5000/search_user",
        allow_redirects=True,
        params={"q": sys.argv[1] if len(sys.argv) == 2 else ""}
    )
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{0}] {1}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
