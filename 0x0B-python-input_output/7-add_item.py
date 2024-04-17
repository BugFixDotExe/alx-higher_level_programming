#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a script that adds all args to a Python list,
and then save them to a file"""
import os
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

tokens = sys.argv[1:]
with open("add_item.json", mode="w", encoding="UTF-8"):
    save_to_json_file(tokens, "add_item.json")
    load_from_json_file("add_item.json")
