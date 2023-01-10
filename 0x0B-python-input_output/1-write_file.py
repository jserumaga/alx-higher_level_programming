#!/usr/bin/python3

"""
number_of_lines function module.
Define number_of_lines function.
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file (UTF8).
    filename (file): the file, must exist, must have permissions
    """
    with open(filename, encoding="UTF-8") as myfile:
        return len(myfile.readlines())
