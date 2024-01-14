#!/usr/bin/env python3

import numpy as np


def multiplication_table(max_value: int):
    a = np.arange(max_value)
    return a * a.reshape(max_value, 1)
    # return np.arange(max_value) * np.arange(max_value).reshape(max_value, 1)


def main():
    print(multiplication_table(4))


if __name__ == "__main__":
    main()
