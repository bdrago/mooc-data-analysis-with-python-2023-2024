#!/usr/bin/env python3

import pandas as pd


def inverse_series(s: pd.Series) -> pd.Series:
    new_series = pd.Series(s.index, index=s.values)
    return new_series


def main():
    d = {2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"}
    s4 = pd.Series(d, name="Presidents")
    # test_list = list("abcdefg")
    # s4 = pd.Series(test_list)
    print(s4)
    s5 = inverse_series(s4)
    print(s5["Bush"])


if __name__ == "__main__":
    main()
