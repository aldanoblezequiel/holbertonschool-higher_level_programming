#!/usr/bin/python3
"""ect etc"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        datum = {'q': argv[1]}
    else:
        datum = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=datum)

    try:
        req = r.json()
        if len(req) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except:
        print("Not a valid JSON")
