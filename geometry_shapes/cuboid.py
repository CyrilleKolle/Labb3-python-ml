from __future__ import annotations
from rectangle import Rectangle


class Cuboid(Rectangle):
    """3D child class from parent Rectangle class representing a rectangular figure
    ```
    Attributes
    ----------
    side1: A float or int representing the height of the cuboid

    side2: A float or int representing the width of the cuboid

    side3: A float or int representing the breadth of the cuboid
    ```
    """

    def __init__(
        self,
        x: float | int,
        y: float | int,
        side1: float | int,
        side2: float | int,
        side3: float | int,
    ) -> None:
        """
        Parameters
        ----------
        side3: represents the breadth or depth of the cuboid
        """
        self.side3 = side3
        """
        super function used to x,y, side1 and side2 from the parent class Rectangle
        """
        super().__init__(x, y, side1, side2)

    @property
    def area(self) -> int | float:
        """Getter function used to retrieve the area of the cuboid. It does not have a getter function so that its value cant be changed"""
        # 2(lb+bh+hl)
        return 2 * (
            (self.side3 * self.side2)
            + (self.side2 * self.side1)
            + (self.side1 * self.side3)
        )

    @property
    def circumference(self) -> int | float:
        """
        A getter function to get the circumference of the cuboid. The property does not have a setter to prevent its value from being changed
        """
        # The perimeter of a cuboid is 4(L+B+H).
        return 4 * (self.side1 + self.side2 + self.side3)

    @property
    def volume(self) -> int | float:
        """
        A getter function for the volume attribute. It returns the volume of a cuboid. It doesnt have a setter to prevent its value from being changed.
        """
        return self.side1 * self.side2 * self.side3

    def is_inside(self, a, b) -> bool:
        """A function to check if point is inside a cuboid"""
        check = (a - self.side1) ** 2 + (b - self.side2) ** 2 < (self.side2 / 2) ** 2
        return check

    def __repr__(self) -> str:
        """__repr__ overrides the parent Rectangle's __repr__ function to return the object representation of a cuboid"""

        return f"cuboid(Area='{self.are}', circumference='{self.circumference}')"

    def __str__(self) -> str:
        """__str__ overrides the Rectangle parent's __str__ to return a string representation of a Cuboid"""

        return f"cuboid with points x = {self.x}, y = {self.y}, an area of {self.area}, a volume = {self.volume} and a circumference of {self.circumference}"
