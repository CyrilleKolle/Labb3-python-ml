from __future__ import annotations
from unicodedata import name
import numpy as np
from abc import abstractmethod


class Shape:
    """A parent class used to represent shapes
    ```
    Atrributes
    ------------------
    x: float or string representing the coordinate point at the center of the shape at the x-axis

    y: float or string representing the coordinate point at the center of the shape at the y-axis
    ```

    """

    """
    __init__ function is called everytime an instance of the class is created. It  lets the class initialize the object's attributes and serves no other purpose
    """

    def __init__(self, x: float | int, y: float | int) -> None:
        """
        Parameters
        ----------
        x: center of shape at x-axis
        y: center of shape at y-axis
        """
        self.x = x
        self.y = y

    @abstractmethod
    def area():
        """An area abstract method that forces all shapes created to have an area"""
        pass

    @abstractmethod
    def circumference():
        """An abstract method compelling all shapes created to have a circumference"""
        pass

    @property
    def x(self) -> int | float:
        """Used to get the attribute x from class shape"""
        return self._x

    @x.setter
    def x(self, value: int | float) -> int | float:
        """Used to set the attribute x from class shape x"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"x coordinate must be an int or float")
        self._x = value

    @property
    def y(self) -> int | float:
        """Used to get the attribute y from class shape y"""
        return self._y

    @y.setter
    def y(self, value: int | float) -> int | float:
        """Used to set the attribute y from class shape y"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"y coordinate must be an int or float")
        self._y = value

    @property
    def midPoint(self) -> tuple:
        """used to get the midpoint of a shape"""
        x = self.x / 2
        y = self.y / 2
        return (x, y)

    def translate(self, a: int | float, b: int | float):
        """Function used to move a shape by given points a and b"""
        value = [a, b]
        for i in range(len(value)):
            if not isinstance(value[i], (float, int)):
                raise TypeError(
                    f"translate numbers have to be ints or float and not {type(value[i]).__name__}"
                )

        self.x += a
        self.y += b

    def __eq__(self, other: Shape) -> bool:
        """__dunder__ function to check if two shapes are equal"""
        # if self.__class__.__name__ != other.__class__.__name__:
        #     raise TypeError("Must be of thesame type")
        return (self.area == other.area) and (self.circumference == other.circumference)

    def __lt__(self, other: Shape) -> bool:
        """__dunder__ function to check if current shape is less than another shape"""
        return (self.area < other.area) and (self.circumference < other.circumference)

    def __gt__(self, other: Shape) -> bool:
        """__dunder__ function to check if current shape is greater than another shape"""
        return (self.area > other.area) and (self.circumference > other.circumference)

    def __le__(self, other: Shape) -> bool:
        """__dunder__ function to check if current shape is less than or equal than another shape"""
        return (self.area <= other.area) and (self.circumference <= other.circumference)

    def __ge__(self, other: Shape) -> bool:
        """__dunder__ function to check if current shape is greater than or equal than another shape"""
        return (self.area >= other.area) and (self.circumference >= other.circumference)

    def __repr__(self) -> str:
        """__repr__ returns the object representation in a string form of a shape"""
        return f"Shape(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        """__str__ returns the string represention of a shape"""
        return f"Shape with midpoint {self.midPoint}"
