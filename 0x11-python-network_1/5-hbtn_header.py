#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below"""

if __name__ == "__main__":
    import requests
    import sys

    content = requests.get(sys.argv[1])
    print(content.headers.get("X-Request-Id"))
