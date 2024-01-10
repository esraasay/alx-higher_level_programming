#!/usr/bin/python3
"""definding read_filr function"""


def read_file(filename=""):
    """Read filename with utf-8"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
