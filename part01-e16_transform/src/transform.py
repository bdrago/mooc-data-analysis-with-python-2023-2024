#!/usr/bin/env python3


def transform(s1, s2) -> list:
    int_list1 = list(map(int, s1.split()))
    int_list2 = list(map(int, s2.split()))
    return [i * j for i, j in zip(int_list1, int_list2)]


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
