#!/usr/bin/python3
"""create a square class that has both size and position"""


class Square:
    """Instance constructor"""
    def __init__(self, size=0, position=(0, 0)):

        self.__position = position
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
    
    @property
    def position(self):
        return self.__position

    """Set the value of private attribute size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Set the value of position"""
    @position.setter
    def position(self, value):
        """sets the private instance attribute position"""
        check = 0
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
            break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Return the value of the area of the square"""
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
