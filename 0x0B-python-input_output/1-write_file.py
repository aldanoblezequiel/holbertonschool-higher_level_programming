#!/usr/bin/python3
"""
Write File Module
"""


def write_file(filename="", text=""):
    """Writes a string to a .txt"""
    with open(filename, 'w', encoding='utf-8') as w:
        return w.write(text)
