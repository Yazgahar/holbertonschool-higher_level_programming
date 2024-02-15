#!/usr/bin/python3
""" load json file """
import json


def load_from_json_file(filename):
    """ load json file """
    with open(filename, 'r') as file:
        r = json.load(file)
    return r
