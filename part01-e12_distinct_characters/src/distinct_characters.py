#!/usr/bin/env python3


def distinct_characters(L) -> dict:
    new_dict = {}
    for string in L:
        new_dict[string] = len(set(string))
    return new_dict


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
