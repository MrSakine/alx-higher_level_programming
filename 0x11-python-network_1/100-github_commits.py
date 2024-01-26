#!/usr/bin/python3
"""
This module lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/$1/$2/commits"
    url = url.replace("$1", sys.argv[1])
    url = url.replace("$2", sys.argv[2])
    req = requests.get(url)
    responses = req.json()
    for response in responses[:10]:
        sha = response["sha"]
        name = response["commit"]["author"]["name"]
        print("{}: {}".format(sha, name))
