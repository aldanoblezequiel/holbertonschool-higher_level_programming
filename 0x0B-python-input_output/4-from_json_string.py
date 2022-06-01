#!/usr/bin/python3
"""
Json Module 2
"""
import json


def from_json_string(my_str):
    """Returns a struct represented by a JSON string"""
    return json.loads(my_str)
