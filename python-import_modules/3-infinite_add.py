#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    sum = 0
    for i in args:
        sum = sum + int(i)
    print(sum)
