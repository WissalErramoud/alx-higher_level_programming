#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints a number of elements in an array (list)

    Args:
        my_list (list): my lisy
        x (int): number of elements to be printed

    Returns:
        print count
    """
    pcount = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            pcount = pcount + 1
        except IndexError:
            break
    print("")
    return (pcount)
