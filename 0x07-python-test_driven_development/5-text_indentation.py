#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for line in text.splitlines():
        line.replace(" ","")
        for i in line:
            print(i, end="")
            if i == '.' or i == '?' or i == ':':
                print("")
                print("")
