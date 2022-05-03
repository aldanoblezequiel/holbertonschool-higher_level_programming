#!/usr/bin/python3
import sys
if __name__ == "__main__":  # Prevent useless code to be executed
    sum = 0
    for i in sys.argv[1:]:
        sum += int(i)
    print("{:d}".format(sum))
