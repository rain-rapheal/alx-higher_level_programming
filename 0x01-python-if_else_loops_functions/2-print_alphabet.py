#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the in lowercase the alphabet, not followed by a new line."""
for letter in range(97, 123):
print("{}".format(chr(letter)), end="")
