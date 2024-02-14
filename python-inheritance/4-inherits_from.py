#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class"""
    if (type(obj) is not a_class and isinstance(obj, a_class)):
        return True
    return False
