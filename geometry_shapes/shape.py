from __future__ import annotations
from unicodedata import name
import numpy as np


class Shape:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y


    @property
    def x(self) -> int | float:
        return self._x

    @x.setter
    def x(self, value: int | float) -> int | float:
        if not isinstance(value, (int, float)):
            raise TypeError(f"x coordinate must be an int or float")
        self._x = value

    @property
    def y(self) -> int | float:
        return self._y

    @y.setter
    def y(self, value: int | float) -> int | float:
        if not isinstance(value, (int, float)):
            raise TypeError(f"y coordinate must be an int or float")
        self._y = value

    @property
    def midPoint(self) -> tuple:
        x = self.x / 2
        y = self.y / 2

        return (x, y)

    def is_inside(self, *other: tuple) -> float:
        mid_point = self.midPoint
        # calculate euclidean distance between midpoint and test point
        distance_to_mid_point = (
            sum((y - x) ** 2 for x, y in zip(mid_point, other)) ** 0.5
        )
        print(distance_to_mid_point)
        print(mid_point)
        if distance_to_mid_point < mid_point[0] or distance_to_mid_point < mid_point[1]:
            return True
        else:
            return False
    

    def __eq__(self, other) -> bool:
        return self.area == other.area and self.circumference == self.circumference

    def __lt__(self, other) -> bool:
        return self.area < other.area 

    def __gt__(self, other) -> bool:
        return self.area > other.area 

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area


    def __repr__(self) -> str:
        return f"Shape(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Shape with midpoint {self.midPoint}"

    def is_(self) -> str:
        if self.__class__.__name__ == "Rectangle":
            print("Rectangle")
        elif self.__class__.name__ == "Circle":
            print("Circle")
        elif self.__class__.__name__ == "Cube":
            print("Cube")
        elif self.__class__.__name__ == "Sphere":
            print("Sphere")

