#!/usr/bin/python3

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

    def uppercase(s):
        for char in s:
            print("{:c}".format(ord(char)) if not islower(char) else chr(ord(char) - 32),
                   end="")
    print()
