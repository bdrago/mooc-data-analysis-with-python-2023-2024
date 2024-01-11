#!/usr/bin/env python3


def merge(L1, L2):
    new_list = []
    i1 = 0
    i2 = 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            new_list.append(L1[i1])
            i1 += 1
        else:
            new_list.append(L2[i2])
            i2 += 1
    if i1 < len(L1):
        new_list.extend(L1[i1:])
    else:
        new_list.extend(L2[i2:])
    return new_list


def main():
    list1 = sorted([2, 5, 4, 8, 12, 6])
    list2 = sorted([3, 1, 7, 9, 11])
    print(merge(list1, list2))


if __name__ == "__main__":
    main()
