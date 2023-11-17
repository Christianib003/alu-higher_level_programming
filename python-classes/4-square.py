#!/usr/bin/python3
"""Creates a square class"""


class Square:
    """Instance constructor"""
    def __init__(self, size=0):

        """Validate size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Get the value of private attribute size"""
    @property
    def size(self):
        return self.__size
    
    """Set the value of private attribute size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Return the value of the area of the square"""
    def area(self):
        return self.__size ** 2
