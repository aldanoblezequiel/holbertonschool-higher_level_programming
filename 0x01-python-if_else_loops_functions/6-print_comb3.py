#!/usr/bin/python3
for j in range(0, 9):
    for i in range(j + 1, 10):
        if j < i:
            print("{}{}".format(j, i), end='')
            if j != 8:
                print(", ", end='')
            else:
                print()
