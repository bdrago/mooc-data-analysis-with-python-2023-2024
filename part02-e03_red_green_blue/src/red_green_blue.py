#!/usr/bin/env python3
"""
Write function red_green_blue that reads the file rgb.txt from the folder src. Remove the irrelevant first line of the file. The function should return a list of strings. Clean-up the file so that the strings in the returned list have four fields separated by a single tab character (\t). Use regular expressions to do this.

The first string in the returned list should be:

'255\t250\t250\tsnow'
"""


import re


def red_green_blue(filename="src/rgb.txt") -> list:
    cleaned_file = []
    pattern = r"\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)"

    with open(filename, "r") as f:
        for line in f:
            if "!" in line:
                continue
            m = re.match(pattern, line)
            n = m.groups()
            cleaned_file.append(n[0] + "\t" + n[1] + "\t" + n[2] + "\t" + n[3])
    return cleaned_file


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()
