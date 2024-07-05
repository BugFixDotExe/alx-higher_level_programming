#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below"""

if __name__ == "__main__":
    import requests
    import sys

    # create payload object
    payload = {}
    payload["email"] = sys.argv[2]
    # create a request using the url and the inteded data
    content = requests.post(sys.argv[1], data=payload)
    print(content.text)
