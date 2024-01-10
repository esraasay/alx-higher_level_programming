#!/usr/bin/python3
"""define function to data structure"""


import json


def save_to_json_file(my_obj, filename):
    """return data structure from json string"""
    with open(filename, encoding="utf-8", mode="w") as f:
        json.dump(my_obj, f)
