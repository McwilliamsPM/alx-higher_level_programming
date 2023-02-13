#!/usr/bin/python3
"""A class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A subclass Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method for rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate
            y (int): y-coordinate
            id (int): id of rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @width.setter
    def width(self, width):
        """setter method for width
        Args:
            width (int): width of rectangle
        Raises:
            TypeError: if `width` is not an integer
            ValueError: if `width` is not greater than 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """setter method for height
        Args:
            height (int): height of rectangle
        Raises:
            TypeError: if `height` is not an integer
            ValueError: if `height` is not greater than 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """setter method for x
        Args:
            x (int): x-coordinate of rectangle
        Raises:
            TypeError: if `x` is not an integer
            ValueError: if `x` is negative
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter method for y
        Args:
            y (int): y-coordinate of rectangle
        Raises:
            TypeError: if `y` is not an integer
            ValueError: if `y` is negative
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of rectangle"""
        return self.width * self.height

    def display(self):
        """displays the # representation of rectangle"""
        rows = self.height
        columns = self.width
        for _ in range(self.y):
            print()
        for r in range(rows):
            print(' ' * self.x, end='')
            for c in range(columns):
                print('#', end='')
            print()

    def __str__(self):
        """Returns string representation of rectangle object"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__,
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes
        Args:
            args: arguments
            kwargs: key-word arguments
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of a rectangle
        Returns:
            dictionary of attributes
        """
        obj_dict = {}
        for k, v in self.__dict__.items():
            if k == '_Rectangle__width':
                obj_dict['width'] = v
            if k == 'id':
                obj_dict['id'] = v
            if k == '_Rectangle__y':
                obj_dict['y'] = v
            if k == '_Rectangle__height':
                obj_dict['height'] = v
            if k == '_Rectangle__x':
                obj_dict['x'] = v
        return obj_dict
