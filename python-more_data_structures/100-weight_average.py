#!/usr/bin/python3


def weight_average(my_list=[]):
    average = 0
    summation = 0
    total_weight = 0

    if not my_list:
        return average
    for pair in my_list:
        summation += pair[0] * pair[1]
        total_weight += pair[1]
        average = summation / total_weight

    return average
