#!/bin/bash
# A Bash script that takes in a URL displays the size of the body of the response.
if [[ "$#" -gt  0 ]]; then
	curl -s --no-verbose "$1" -w "%{size_download}\n"
else
	exit 1
fi
