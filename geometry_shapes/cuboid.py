from __future__ import annotations
from rectangle import Rectangle


class Cuboid(Rectangle):
    """child class from parent Rectangle class representing a rectangular figure
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

        self.side3 = side3
        super().__init__(x, y, side1, side2)


    @property
    def area(self) -> int | float:
        # 2(lb+bh+hl)
        return 2 * (
                (self.side3 * self.side2)
                + (self.side2 * self.side1)
                + (self.side1 * self.side3)
            )

    @property
    def circumference(self) -> int | float:
        #The perimeter of a cuboid is 4(L+B+H).
        return 4 * (self.side1 + self.side2 + self.side3)

    @property
    def volume(self) -> int | float:
        return self.side1 * self.side2 * self.side3

    def __repr__(self) -> str:
        return f"cuboid(Area='{self.are}', circumference='{self.circumference}')"

    def __str__(self) -> str:
        return f"cuboid with an area of {self.area} and a circumference of {self.circumference}"
