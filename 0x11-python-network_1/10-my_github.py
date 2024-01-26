#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": "Bearer {}".format(sys.argv[2])
    }
    req = requests.get(url="https://api.github.com/user", headers=headers)
    response = req.json()
    try:
        print(response["id"])
    except KeyError:
        print(None)
