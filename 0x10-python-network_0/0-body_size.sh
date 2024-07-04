#!/bin/bash
# A Bash script that takes in a URL displays the size of the body of the response.
curl -s -w '%{size_download}\n' -o /dev/null "$1"
