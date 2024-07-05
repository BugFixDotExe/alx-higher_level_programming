#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a Python script that takes in a lette
    and sends a POST request to
    http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    content = requests.post(
            "http://0.0.0.0:5000/search_user", data={'q': sys.argv[1]})
    content = content.json()
    if (len(content) == 0):
        print("No result")
    else:
        print("[{}] {}".format(content.get("id"), content.get("name")))
