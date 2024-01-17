#!/usr/bin/python3

import numpy as np


def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    """Write function meeting_planes that gets the coefficients of three planes as parameters and returns the point where the planes meet. The equations for the planes are"""
    # Create the matrix
    A = np.array([[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]])
    # Create the vector
    b = np.array([[-1], [-1], [-1]])
    # Solve the system

    x = np.linalg.solve(A, b)
    return x.ravel()


def main():
    a1 = 1
    b1 = 4
    c1 = 5
    a2 = 3
    b2 = 2
    c2 = 1
    a3 = 2
    b3 = 4
    c3 = 1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")


if __name__ == "__main__":
    main()
