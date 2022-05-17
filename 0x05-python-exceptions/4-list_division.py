#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = []
    for n in range(0, list_length):
        res = 0
        try:
            res = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        finally:
            ret_list.append(res)
    return ret_list
