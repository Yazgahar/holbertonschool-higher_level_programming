#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return my_copy
    my_copy[idx] = element
    return my_copy
