#!/usr/bin/env python3
import pandas as pd


def read_series() -> pd.Series:
    user_data = {}
    while True:
        user_input = input("Enter index and value: ")
        if user_input:
            try:
                key, value = user_input.split()
                user_data[key] = value
            except:
                raise ValueError("invalid user entry")
        else:
            break

    return pd.Series(user_data)


def main():
    read_series()


if __name__ == "__main__":
    main()
