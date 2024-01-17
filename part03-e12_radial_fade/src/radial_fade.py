#!/usr/bin/env python3

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


def center(a):
    return ((a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2)


def radial_distance(a: np.ndarray) -> np.ndarray:
    """
    for an image with width w and height h an array with shape (h,w), where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image
    """
    c = np.array(center(a))
    y, x = np.indices(a.shape[:2])
    distance = np.sqrt((x - c[1]) ** 2 + (y - c[0]) ** 2)
    return distance


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    return scale(1 - radial_distance(a))


def radial_fade(a):
    return np.array(a * radial_mask(a)[:, :, None])


def main():
    painting = plt.imread("src/painting.png")
    mask = radial_mask(painting)
    faded = radial_fade(painting)

    fig, ax = plt.subplots(1, 3)
    ax[0] = plt.imshow(painting)
    ax[1] = plt.imshow(mask)
    ax[2] = plt.imshow(faded)
    plt.show()


if __name__ == "__main__":
    main()
