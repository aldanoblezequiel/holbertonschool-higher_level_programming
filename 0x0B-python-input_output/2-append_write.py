#!/usr/bin/python3
"""
Append Module
"""


def append_write(filename="", text=""):
    """Appends a string at the bottom of a .txt"""
    with open(filename, 'a', encoding='utf-8') as app:
        return app.write(text)
