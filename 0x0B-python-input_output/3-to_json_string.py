#!/usr/bin/python3
"""defindig function to jons string"""


import json


def to_json_string(my_obj):
    """returns a json string representation of an object"""
    return json.dumps(my_obj)
