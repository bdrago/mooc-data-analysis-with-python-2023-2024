#!/usr/bin/env python3

"""
Write function file_listing that loads the file src/listing.txt. It should return a list of tuples (size, month, day, hour, minute, filename). Use regular expressions to do this (either match, search, findall, or finditer method).

An example: for line

-rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf

the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf").

"""
import re


def file_listing(filename="src/listing.txt"):
    output_list = []

    with open(filename, "r") as f:
        for line in f:
            # match the first
            matches = re.search(
                r"\b([0-9]+) ([A-Z][a-z][a-z]) \s*(\d{1,2}) (\d{2})\:(\d{2}) (\S+\b)",
                line,
            )
            g = matches.groups()
            output_list.append((int(g[0]), g[1], int(g[2]), int(g[3]), int(g[4]), g[5]))

    return output_list


def main():
    results = file_listing()
    for i in results:
        print(i)


if __name__ == "__main__":
    main()
