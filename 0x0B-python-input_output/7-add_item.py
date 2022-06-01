#!/usr/bin/python3
"""
Module addition
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile('add_item.json'):
    obj_file = load_from_json_file('add_item.json')
else:
    obj_file = []
for n in range(1, len(sys.argv)):
    obj_file.append(sys.argv[n])

save_to_json_file(obj_file, 'add_item.json')
