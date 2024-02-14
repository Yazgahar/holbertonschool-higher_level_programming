#!/usr/bin/python3
"""
Define MyList class
"""


class MyList(list):
    def print_sorted(self):
        """
        Sort the elements of MyList object using the built-in sorted function
        """
        sorted_list = sorted(self)
        print(sorted_list)
