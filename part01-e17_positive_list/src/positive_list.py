#!/usr/bin/env python3


def positive_list(list_of_numbers: list) -> list:
    return list(filter(lambda x: x > 0, list_of_numbers))


def main():
    print(positive_list([2, -2, 0, 1, -7]))


if __name__ == "__main__":
    main()
