#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Iterate through each character in the input text
    for char in text:
        # Append the character to the formatted_text
        formatted_text += char

        # Add two new lines after '.', '?', and ':'
        if char in ['.', '?', ':']:
            formatted_text += '\n\n'

    # Print the formatted text with leading and trailing whitespaces removed
    print(formatted_text.strip())
