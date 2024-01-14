#!/usr/bin/env python3

import sys
from statistics import mean, stdev


def summary(filename: str) -> tuple:
    nums = []
    with open(filename, "r") as f:
        for line in f:
            try:
                nums.append(float(line))
            except:
                ValueError("line did not contain a valid number")
    sums = sum(nums)
    average = mean(nums)
    std_dev = stdev(nums)
    return (sums, average, std_dev)


def main():
    for file in sys.argv[1:]:
        results = summary(file)
        output = f"File: {file} Sum: {results[0]:.6f} Average: {results[1]:.6f} Stddev: {results[2]:.6f}"
        print(output)


if __name__ == "__main__":
    main()
