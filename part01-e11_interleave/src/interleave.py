#!/usr/bin/env python3


def interleave(*lists):
    new_list = []
    for list in zip(*lists):
        new_list.extend(list)
    return new_list


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ["a", "b", "c"]))


if __name__ == "__main__":
    main()
