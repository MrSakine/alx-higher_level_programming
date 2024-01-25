#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -H "Content-Type: application/json" --data "$(cat $2)" $1
