#!/usr/bin/python3
"""
Read File Module
"""


def read_file(filename=""):
    """Writes a string to a .txt"""
    with open(filename, encoding='utf-8') as o:
        for line in o:
            print(line, end="")
