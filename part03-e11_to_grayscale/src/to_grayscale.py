#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def to_grayscale(rgb_image: np.ndarray) -> np.ndarray:
    # code goes here
    weights = np.array([0.2126, 0.7152, 0.0722])
    gs_image = np.dot(rgb_image, weights)
    return gs_image


def to_red(rgb_image: np.ndarray) -> np.ndarray:
    return np.array(rgb_image * [1, 0, 0])


def to_green(rgb_image: np.ndarray) -> np.ndarray:
    return np.array(rgb_image * [0, 1, 0])


def to_blue(rgb_image: np.ndarray) -> np.ndarray:
    return np.array(rgb_image * [0, 0, 1])


def main():
    painting = plt.imread("painting.png")
    # gs_painting = to_grayscale(painting)
    # plt.gray()
    # plt.imshow(gs_painting)
    # plt.show()

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting))
    ax[2].imshow(to_blue(painting))
    plt.show()


if __name__ == "__main__":
    main()
