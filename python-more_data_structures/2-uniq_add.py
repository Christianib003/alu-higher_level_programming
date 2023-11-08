#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    used_num = []
    i = 0
    while i < len(my_list):
        if my_list[i] not in used_num:
            sum += my_list[i]
            used_num.append(my_list[i])
        i += 1
    return sum
