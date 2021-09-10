from collections import namedtuple
from typing import Tuple

Point = namedtuple("Point", ["x", "y"])


def get_square(a: Point, b: Point) -> Tuple[Point, Point]:
    """
    (대충 2개의 인접하지 않는 점이 주어지면 그 두점으로 정사각형 나머지 두 점 돌려주는 함수)
    """

    def middle(x1, x2) -> float:
        return (x1 + x2) / 2

    def half_diagonal(x1, x2) -> float:
        return (x1 - x2) / 2

    return Point(
        middle(a.x, b.x) - half_diagonal(a.y, b.y), middle(a.y, b.y) + half_diagonal(a.x, b.x)
    ), Point(middle(a.x, b.x) + half_diagonal(a.y, b.y), middle(a.y, b.y) - half_diagonal(a.x, b.x))


print(get_square(Point(1, 1), Point(2, 2)))
