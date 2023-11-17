#!/usr/bin/python3
"""Creates a class with a private attribute"""


class Square:
    """init method with a private attribute"""

    def __init__(self, size):
        self.__size = size
