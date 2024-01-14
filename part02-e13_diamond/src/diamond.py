#!/usr/bin/env python3

import numpy as np


def diamond(n):
    matrix = np.eye(n, dtype=int)
    t_matrix = matrix[1:, ::-1]
    right_side = np.concatenate((matrix, t_matrix))
    left_side = right_side[:, :0:-1]
    return np.concatenate((left_side, right_side), axis=1)


def main():
    pass


if __name__ == "__main__":
    main()
