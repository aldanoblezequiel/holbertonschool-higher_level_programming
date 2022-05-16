#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    large = 0
    i = 0
    try:
        for i in my_list:
            if (large < x):
                print(i, end="")
                large += 1
        print()
    finally:
        return (large)
