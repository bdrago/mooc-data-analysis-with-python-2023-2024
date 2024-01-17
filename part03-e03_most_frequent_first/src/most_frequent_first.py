#!/usr/bin/env python3

import numpy as np
from icecream import ic


def most_frequent_first(a, c):
    """
    Write function most_frequent_first that gets a two dimensional array and an index c of a column as parameters. The function should then return the array whose rows are sorted based on column c, in the following way. Rows are ordered so that those rows with the most frequent element in column c come first, then come the rows with the second most frequent element in column c, and so on. Therefore, the values outside column c don't affect the ordering in any way.
    """

    # Get the column
    column = a[:, c]

    # Get the unique values and their counts
    unique, counts = np.unique(column, return_counts=True)
    ic(unique)
    ic(counts)

    # Get the indexes of the sorted counts
    sorted_counts_indexes = np.argsort(counts)[::-1]
    ic(sorted_counts_indexes)

    # Get the unique values sorted by their counts
    sorted_unique = unique[sorted_counts_indexes]
    ic(sorted_unique)

    # Get the indexes all the numbers in column in
    # the order of sorted_unique
    indexes = np.where(sorted_unique == column[:, None])
    ic(indexes)

    # Get the sorted array
    sorted_column = np.array(
        sorted(column, key=lambda x: np.where(sorted_unique == x)[0][0])
    )

    return sorted_column


if __name__ == "__main__":
    a = np.array(
        [
            [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
            [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
            [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
            [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
            [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
            [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
            [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
            [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
            [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
            [5, 9, 3, 0, 5, 0, 1, 2, 4, 2],
        ]
    )

    print(most_frequent_first(a, -1))
