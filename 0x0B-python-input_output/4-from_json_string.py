#!/usr/bin/python3
"""define function to data structure"""

import json


def from_json_string(my_str):
    """return data structure from json string"""
    return json.loads(my_str)
