#!/bin/bash
# A Bash script that takes in a URL displays the size of the body of the response.
curl -s "$1" -w '%{size_download}\n'
