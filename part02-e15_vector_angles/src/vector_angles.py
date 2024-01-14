#!/usr/bin/env python3
"""
Write function vector_angles that gets two arrays X and Y with same shape (n,m) as parameters. Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) with the corresponding angles between vectors of X and Y in degrees, not in radians
"""
import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    inner = np.sum(X * Y, axis=1)
    x_u = np.linalg.norm(X, axis=1)
    y_u = np.linalg.norm(Y, axis=1)
    cos = inner / (x_u * y_u)
    return np.rad2deg(np.arccos(np.clip(cos, -1, 1)))6


def main():
    np.random.seed(9)
    a = np.random.randint(0, 10, (3, 4))
    b = np.random.randint(0, 10, (3, 4))
    print(vector_angles(a, b))


if __name__ == "__main__":
    main()
