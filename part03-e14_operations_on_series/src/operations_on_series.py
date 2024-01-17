#!/usr/bin/env python3
import pandas as pd


def create_series(list1: list, list2: list) -> (pd.Series, pd.Series):
    INDICIES = list("abc")

    s1 = pd.Series(list1, index=INDICIES)
    s2 = pd.Series(list2, index=INDICIES)

    return (s1, s2)


def modify_series(s1: pd.Series, s2: pd.Series) -> (pd.Series, pd.Series):
    s1["d"] = s2["b"]
    del s2["b"]
    return (s1, s2)


def main():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    s1, s2 = create_series(nums1, nums2)
    s3, s4 = modify_series(s1, s2)
    print(s3)
    print(s4)
    print(s3 + s4)


if __name__ == "__main__":
    main()
