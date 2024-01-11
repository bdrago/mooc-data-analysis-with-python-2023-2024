#!/usr/bin/env python3


def find_matching(list_strings: list, pattern: str) -> list:
    results = []
    for i, word in enumerate(list_strings):
        if pattern in word:
            results.append(i)
    return results


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
