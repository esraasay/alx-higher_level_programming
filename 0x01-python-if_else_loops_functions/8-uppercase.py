#!/usr/bin/python3

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

    def uppercase(s):
        for char in s:
            upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(upper_char), end="")
    print()
