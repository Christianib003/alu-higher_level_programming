#!/usr/bin/python3


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

    def my_print(self):
        """Print the square using #"""
        i = 1
        while i <= self.__size:
            j = 1
            while j <= self.__size:
                if j == self.__size:
                    print("#")
                else:
                    print("#", end="")
                j += 1
            i += 1
