#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0
    prev_value = 0

    for num in reversed(roman_string):
        value = roman_int[num]

        if value < prev_value:
            number -= value
        else:
            number += value

        prev_value = value

    return number
