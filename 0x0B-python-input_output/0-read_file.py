#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
