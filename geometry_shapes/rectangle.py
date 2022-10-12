from __future__ import annotations
import math
from matplotlib import pyplot as patches
from shape import Shape


class Rectangle(Shape):
    """child class from parent Shape class representing a rectangular figure
    ```
    Attributes
    ----------
    side1: A float or int representing the height of the rectangle

    side2: A float or int representing the width of the rectangle
    ```

    """

    def __init__(
        self, x: float | int, y: float | int, side1: float | int, side2: float | int
    ) -> None:
        """
        __init__ function is called everytime an instance of the class is created. It  lets the class initialize the object's attributes and serves no other purpose
        """

        """side 1 represents height"""
        self.side1 = side1

        """side 2 represents width"""
        self.side2 = side2

        """A super function so that rectangle can have access to parent class shape's x and y"""
        super().__init__(x, y)

    @property
    def side1(self) -> int | float:
        """Used to get the attribute side1 or height from class Rectangle"""
        return self._side1

    @side1.setter
    def side1(self, value: (int | float)):
        """Used to set the attribute side1 of class Rectangle"""
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"side 1 of rectangle must be a float or int and not {type(value).__name__}"
            )
        self._side1 = value

    @property
    def side2(self) -> int | float:
        """
        Used to get the attribute side2 or width from class Rectangle
        """
        return self._side2

    @side2.setter
    def side2(self, value: (int | float)):
        """Used to set the attribute side1 of class Rectangle"""
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"side 2 of rectangle must be a float or int and not {type(value).__name__}"
            )
        self._side2 = value

    def validate_rectangle(self):
        """Function used to check that a rectangle's sides are not equal otherwise its a not a rectangle"""
        if self.side1 == self.side2:
            raise ValueError("Rectangles sides must differ")
        return self.side1 != self.side2

    @property
    def area(self):
        """A getter to retrieve the area of the rectangle instance. It is a property without a setter so that its value cant be changed"""
        if self.validate_rectangle:
            return self.side1 * self.side2

    def is_inside(self, a, b) -> bool:
        """A function to check if point is inside a rectangle"""
        x_bottom = self.x - (self.side2 / 2)
        y_bottom = self.y - (self.side1 / 2)
        x_top = self.x + (self.side2 / 2)
        y_top = self.y + (self.side1 / 2)

        return (x_bottom <= a <= x_top) and (y_bottom <= b <= y_top)

    @property
    def circumference(self):
        """
        A getter function to retrieve the circumference of the rectangle. It does not have a setter so that its value cant be changed
        """
        if self.validate_rectangle:
            perimetr = (self.side1 * 2) + (self.side2 * 2)
            return perimetr

    def is_square(self) -> bool:
        """A function to check if shape is a square and not rectangle"""
        if self.validate_rectangle:
            diagonal_rect = math.sqrt(self.side1**2 + self.side2**2)
            diagonal_square_1 = math.sqrt((self.side1**2) * 2)
            diagonal_square_2 = math.sqrt((self.side2**2) * 2)

            return diagonal_rect == diagonal_square_1 == diagonal_square_2

    def __repr__(self) -> str:
        """__repr__ overrides the parent Shape classe's __repr__ to return the object representation in a string of a Rectangle"""
        return f"Rectangle(Area={self.area}, Circumference={self.circumference})"

    def __str__(self) -> str:
        """__str__ overrides the Rectangle parent's __str__ to return a string representation of a Rectangle"""

        return f"Rectangle with points x = {self.x}, y = {self.y}, an area of {self.area} and a circumference of {self.circumference}"

    def plot(self, ax):
        """A plot function to plot an intance of a Rectangle created"""
        rect = patches.Rectangle(
            (self.x, self.y), self.side1, self.side2, color="green", fill=False
        )
        ax.add_patch(rect)
