#!/usr/bin/env python3

import numpy as np


def column_comparison(a: np.array) -> np.array:
    """
    Write function column_comparison that gets a two dimensional array as parameter. The function should return a new array containing those rows from the input that have the value in the second column larger than in the second last column. You may assume that the input contains at least two columns.
    """
    c = a[a[:, 1] > a[:, -2]]
    return c


def main():
    # test = np.array(
    #     [[8, 9, 3, 8, 8][0, 5, 3, 9, 9][5, 7, 6, 0, 4][7, 8, 1, 6, 2][2, 1, 3, 5, 8]]
    # )
    test = np.array(
        [
            [8, 9, 3, 8, 8],
            [0, 5, 3, 9, 9],
            [5, 7, 6, 0, 4],
            [7, 8, 1, 6, 2],
            [2, 1, 3, 5, 8],
        ]
    )
    print(column_comparison(test))


if __name__ == "__main__":
    main()
