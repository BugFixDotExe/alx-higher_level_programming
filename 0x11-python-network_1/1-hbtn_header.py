#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
