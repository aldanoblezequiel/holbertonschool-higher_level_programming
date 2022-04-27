#!/usr/bin/python3
def uppercase(str):
    for aux in str:
        aux = ord(aux)
        if aux < 123 and aux > 96:
            aux = aux - 32
        print("{:c}".format(aux), end='')
    print()
