#!/usr/bin/python3
"""Define object attribute lookup function."""


def lookup(obj):
    """Return a list ofobject's available attributes."""
    return (dir(obj))
