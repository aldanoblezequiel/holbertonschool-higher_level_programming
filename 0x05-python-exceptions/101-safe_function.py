#!/usr/bin/python3


from sys import stderr


def safe_function(fct, *args):
    try:
        saf = fct(*args)
    except Exception as er:
        stderr.write("Exception: {}\n".format(er))
        saf = None
    return saf
