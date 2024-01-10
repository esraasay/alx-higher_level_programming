#!/usr/bin/python3
"""definding write_file function"""


def write_file(filename="", text=""):
    """write filename with utf-8"""
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(text)
        return len(text)
