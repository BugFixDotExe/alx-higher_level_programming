#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A Python script that takes your GitHub
credentials (username and password) and
uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    try:
        basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
        content = requests.get("https://api.github.com/user", auth=basic)
        print(content.json().get("id"))
    except ValueError as e:
        print("None")
