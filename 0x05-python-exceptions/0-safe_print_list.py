#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x of the list.

    Args:
        my_list (list): print x values from thid list.
        x (int): The number of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
