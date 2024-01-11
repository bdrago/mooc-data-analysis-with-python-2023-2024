# Enter you module contents here
""" Module to compute hypotenuse and area of right triangle"""


from math import sqrt

__version__ = "1.0"

__author__ = "bdrago"


def hypotenuse(side1: float, side2: float) -> float:
    """returns the length of the hypotenuse when given the
    lengths of two other sides of a right-angled triangle"""
    return sqrt(side1**2 + side2**2)


def area(side1: float, side2: float) -> float:
    """returns the area of the right-angled triangle, when two
    sides, perpendicular to each other, are given as parameters."""
    return (side1 * side2) / 2
