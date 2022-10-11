from __future__ import annotations
from rectangle import Rectangle


class Cube(Rectangle):
    def __init__(
        self, x: float | int, y: float | int, side1: float | int, side2: float | int
    ) -> None:
        super().__init__(x, y, side1, side2)

    def validate_cube(self):
        if self.side1 != self.side2:
            raise ValueError(f"A cube has all its sides equal to each other")

    def validate_other(self, other: Cube):
        if self.side1 != self.side2 and self.area != other.area and self.circumference:
            raise ValueError(f"A cube has all its sides equal to each other")

    @property
    def area(self) -> int | float:
        if self.validate_cube:
            return 6 * self.side1**2

    @property
    def circumference(self) -> int | float:
        if self.validate_cube:
            return 12 * self.side1

    def __repr__(self) -> str:
        return f"Cube(Area='{self.are}', circumference='{self.circumference}')"

    def __str__(self) -> str:
        return (
            f"Cube with an area of {self.area} and a circumference of {self.circumference}"
        )


cube = Cube(1, 2, 3, 2)
cube1 = Cube(1, 1, 3, 3)
print(cube.area)
print(cube1.circumference)
print(cube == cube1)
