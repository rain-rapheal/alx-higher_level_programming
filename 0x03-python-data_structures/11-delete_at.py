#!/usr/bin/python3
# 11-delete_at.py


def delete_at(my_list=[], idx=0):
    """To Delete an item at a specific position of the list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
