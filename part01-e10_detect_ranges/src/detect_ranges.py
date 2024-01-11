#!/usr/bin/env python3


def detect_ranges(original_list: list) -> list:
    L = sorted(original_list)
    new_list = []
    is_range = False
    start = None
    for i, num in enumerate(L):
        if i == len(L) - 1 or L[i] != L[i + 1] - 1:
            if is_range:
                new_list.append((start, num + 1))
                is_range = False
                start = None
            else:
                new_list.append(num)
        else:
            if is_range:
                continue
            else:
                is_range = True
                start = num

    return new_list


def main():
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
