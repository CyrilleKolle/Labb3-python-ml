from __future__ import annotations
import math
from matplotlib import pyplot as plt, patches
from shape import Shape


class Rectangle(Shape):
    """Class representing a rectangular figure"""

    def __init__(
        self, x: float | int, y: float | int, side1: float | int, side2: float | int
    ) -> None:
        self.side1 = side1
        self.side2 = side2
        super().__init__(x, y)

        # if self.side1 or self.side2 == None:
        #     raise ValueError(f"Rectangle must have a side1 and side 2")

    @property
    def side1(self) -> int | float:
        return self._side1

    @side1.setter
    def side1(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"side 1 of rectangle must be a float or int and not {type(value).__name__}"
            )
        self._side1 = value

    @property
    def side2(self) -> int | float:
        return self._side2

    @side2.setter
    def side2(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"side 2 of rectangle must be a float or int and not {type(value).__name__}"
            )
        self._side2 = value

    def validate_rectangle(self):
        if self.side1 == self.side2:
            raise ValueError("Rectangles sides must differ")

    @property
    def area(self):
        if self.validate_rectangle:
            return self.side1 * self.side2

    @property
    def circumference(self):
        if self.validate_rectangle:
            perimetr = (self.side1 * 2) + (self.side2 * 2)
            return perimetr

    def is_square(self) -> bool:
        if self.validate_rectangle:
            diagonal_rect = math.sqrt(self.side1**2 + self.side2**2)
            diagonal_square_1 = math.sqrt((self.side1**2) * 2)
            diagonal_square_2 = math.sqrt((self.side2**2) * 2)

            return diagonal_rect == diagonal_square_1 == diagonal_square_2

    def __repr__(self) -> str:
        return f"Rectangle(Area={self.area}, Circumference={self.circumference})"

    def __str__(self) -> str:
        return f"Rectangle with an area of {self.area} and a circumference of {self.circumference}"

    def plot(self,ax):

        rect = patches.Rectangle(
            (self.x, self.y), self.side1, self.side2, color="green", fill=False
        )
        ax.add_patch(rect)
        



