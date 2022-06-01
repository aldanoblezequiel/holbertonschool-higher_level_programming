#!/usr/bin/python3
"""
Save JsON Module
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object in txt"""
    with open(filename, 'w', encoding="utf-8") as wo:
        wo.write(json.dumps(my_obj))
