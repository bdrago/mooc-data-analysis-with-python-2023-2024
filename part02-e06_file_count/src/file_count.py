#!/usr/bin/env python3

import sys


def file_count(filename: str) -> tuple:
    lines = 0
    words = 0
    chars = 0

    with open(filename, "r") as f:
        for line in f:
            lines += 1
            chars += len(line)
            words += len(line.split())
    return (lines, words, chars)


def main():
    for file in sys.argv[1:]:
        counts = file_count(file)
        output_str = f"{counts[0]}\t{counts[1]}\t{counts[2]}\t{file}"
        print(output_str)


if __name__ == "__main__":
    main()
