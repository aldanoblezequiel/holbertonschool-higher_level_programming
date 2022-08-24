#!/usr/bin/python3
"""Url ect etc"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
