#!/usr/bin/python3
def printed_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
