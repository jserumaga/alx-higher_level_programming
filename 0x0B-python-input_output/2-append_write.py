#!/usr/bin/python3

"""
read_lines function module.
Define read_lines function.
"""


def read_lines(filename="", nb_lines=0):
    """Prints the number of lines specified of a text file (UTF8).
    filename (str): the file, must exist, must have permissions.
    nb_lines (int), default=0: the number of lines to print.
    """
    with open(filename, encoding="UTF-8") as myfile:
        count = 0
        for line in myfile:
            if nb_lines <= 0 or count < nb_lines:
                print(line, end="")
                count += 1
