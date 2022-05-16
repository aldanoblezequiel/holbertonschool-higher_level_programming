#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    size = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (IndexError, TypeError):
            break
        size += 1
    print()
    return size
