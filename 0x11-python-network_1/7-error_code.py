#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below plus"""
"""It has a try and except built in..YEahh!! """

if __name__ == "__main__":
    import requests
    import sys

    # create a request using the url
    # using a try and except block
    # negate all exceptions
    # yes i used my username follow me on github:
    # @bugfixdotexe
    try:
        content = requests.get(sys.argv[1])
        content.raise_for_status()
        print(content.text)
    except requests.exceptions.HTTPError as bugfixdotexe:
        print("Error code: {}".format(bugfixdotexe.args[0].split()[0]))
