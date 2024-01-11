#!/usr/bin/env python3


def sum_equation(L) -> str:
    if L == []:
        return "0 = 0"
    return f"{' + '.join([str(word) for word in L])} = {sum(L)}"


def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation(""))


if __name__ == "__main__":
    main()
