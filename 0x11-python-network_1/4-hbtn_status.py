#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script that fetchs a url"""
"""prints In the format or manner presented below"""

if __name__ == "__main__":
    import requests
    content = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(content.text), content.text))
