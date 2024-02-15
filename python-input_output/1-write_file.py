#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_char = file.write(text)
    return nb_char
