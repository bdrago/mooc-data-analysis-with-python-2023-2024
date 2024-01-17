#!/usr/bin/python3

import numpy as np
from numpy.linalg import LinAlgError


def meeting_lines(a1, b1, a2, b2):
    """
    Write function meeting_lines that gets the coefficients of two lines as parameters and returns the point where the two lines meet. The equations for the lines are
    y = a1*x + b1
    y = a2*x + b2
    Use the numpy.linalg.solve function to solve the system of equations.
    """
    # Create the matrix
    A = np.array([[a1, -1], [a2, -1]])
    # Create the vector
    b = np.array([[-b1], [-b2]])
    # Solve the system
    try:
        x = np.linalg.solve(A, b)
        return x
    except LinAlgError as e:
        raise LinAlgError("The lines do not meet at a single point.") from e
    return []


def main():
    a1 = 1
    b1 = 4
    a2 = 3
    b2 = 2

    x, y = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")


if __name__ == "__main__":
    main()
