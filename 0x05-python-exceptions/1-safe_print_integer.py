#!/usr/bin/python3


def safe_print_integer(value):
    """Print the integer with the "{:d}".format().

    Args:
        value (int): Of the integer to print.

    Returns:
        If ValueError occurs or TypeError print - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
