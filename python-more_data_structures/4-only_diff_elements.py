#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff_elements = set(())
    for element in set_1:
        if element not in set_2:
            diff_elements.add(element)
    for element in set_2:
        if element not in diff_elements and element not in set_1:
            diff_elements.add(element)
    return diff_elements
