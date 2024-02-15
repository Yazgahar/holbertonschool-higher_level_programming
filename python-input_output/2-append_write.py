#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """ append write """
    with open(filename, 'a', encoding='utf-8') as file:
        r = file.write(text)
    return r
