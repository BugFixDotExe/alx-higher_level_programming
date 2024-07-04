#!/bin/bash
# A Bash script that takes in a URL displays the size of the body of the response.
curl -s --no-verbose "$1" -w "%{size_download}\n"
