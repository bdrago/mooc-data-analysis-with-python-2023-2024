#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a: np.array) -> np.array:
    c = int(a.shape[1] / 2)
    b = a[:, :c]
    d = a[:, c:]
    e = np.sum(b, axis=1)
    f = np.sum(d, axis=1)
    g = e > f
    return a[g]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
