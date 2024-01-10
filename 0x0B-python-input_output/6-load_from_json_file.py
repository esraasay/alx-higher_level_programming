#!/usr/bin/python3
"""define function to data structure"""


import json


def load_from_json_file(filename):
    """return data structure from json string"""
    with open(filename, encoding="utf-8", mode="r") as f:
        return json.load(f)
