#!/usr/bin/python3
"""definding append_file function"""


def append_write(filename="", text=""):
    """append filename with utf-8"""
    with open(filename, encoding="utf-8", mode="a") as f:
        f.write(text)
        return len(text)
