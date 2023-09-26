#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for value in my_list:
            if isinstance(value, int):
                print("{:d}".format(value), end='')
                count += 1
                if count == x:
                    break
    except TypeError:
        pass

    print()

    return count
