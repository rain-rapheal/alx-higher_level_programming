#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """To Remove all characters c and C."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
