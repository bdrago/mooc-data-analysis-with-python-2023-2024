#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def subfigures(a):
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(a[:, 0], a[:, 1])
    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()


def main():
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    subfigures(a)


if __name__ == "__main__":
    main()
