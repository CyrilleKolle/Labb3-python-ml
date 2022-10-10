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

    # perimeter is P=2l+2w and area is A=lw where l is the length and w is the width.
    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        perimetr = (self.side1 * 2) + (self.side2 * 2)
        return perimetr

    def is_square(self) -> bool:
        diagonal_rect = math.sqrt(self.side1**2 + self.side2**2)
        diagonal_square_1 = math.sqrt((self.side1**2) * 2)
        diagonal_square_2 = math.sqrt((self.side2**2) * 2)

        return diagonal_rect == diagonal_square_1 == diagonal_square_2

    def __lt__(self, other: Rectangle) -> bool:
        return self.perimeter < other.perimeter

    def __gt__(self, other: Rectangle) -> bool:
        return self.perimeter > other.perimeter

    def __le__(self, other: Rectangle) -> bool:
        return self.perimeter <= other.perimeter

    def __ge__(self, other: Rectangle) -> bool:
        return self.perimeter >= other.perimeter

    def __repr__(self) -> str:
        return f"Rectangle(Area={self.area}, Perimeter={self.perimeter})"

    def __str__(self) -> str:
        return f"Rectangle with an area of {self.area} and a perimeter of {self.perimeter}"

    def __eq__(self, other: Rectangle) -> bool:
        # For two rectangles to be similar, their sides have to be proportional (form equal ratios).
        rect_ratio = self.side1 / self.side2
        test_ratio = other.side1 / other.side2
        return rect_ratio == test_ratio
    

    def plot(self):
        if self.is_shape_circle():
            plt.rcParams["figure.figsize"] = [8, 8]
            plt.rcParams["figure.autolayout"] = True
            fig = plt.figure()
            ax = fig.add_subplot()
            rect = patches.Rectangle((self.x, self.y), self.side1,self.side2, color="green", fill=True)
            ax.add_patch(rect)
            ax.axis("equal")
            return ax
        #return plt.show()
 

rect1 = Rectangle( 1, 2, 2, 1)

# print(rect1.is_square())
