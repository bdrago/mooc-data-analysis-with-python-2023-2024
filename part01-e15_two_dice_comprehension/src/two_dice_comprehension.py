#!/usr/bin/env python3


def main():
    results = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    for line in results:
        print(line)


if __name__ == "__main__":
    main()
