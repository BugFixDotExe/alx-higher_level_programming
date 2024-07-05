#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a python script take in an url and displays"""
"""In the format or manner presented below utf-8"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    # create a request using the url
    # using a try and except block
    # negate all exceptions
    # yes i used my username follow me on github:
    # @bugfixdotexe
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as bugfixdotexe:
        print("Error code: {}".format(bugfixdotexe.code))
