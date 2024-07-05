#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script that fetchs a url"""
"""prints In the format or manner presented below"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
                    type(content),
                    content,
                    content.decode('utf-8')))
